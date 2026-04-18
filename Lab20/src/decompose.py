
import warnings
from typing import Any

import numpy as np
import pandas as pd
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.stattools import adfuller, kpss

try:
    import ruptures as rpt
except ImportError:
    rpt = None


def _validate_series(series: pd.Series, require_positive: bool = False) -> pd.Series:
    if not isinstance(series, pd.Series):
        raise TypeError("series must be a pandas Series.")
    if not isinstance(series.index, pd.DatetimeIndex):
        raise TypeError("series must have a DatetimeIndex.")

    s = series.sort_index().dropna().copy()
    if s.empty:
        raise ValueError("series is empty after dropping missing values.")
    if require_positive and (s <= 0).any():
        raise ValueError("series must be strictly positive.")
    return s


def _infer_stationarity_regression(series: pd.Series) -> str:
    s = series.dropna()
    if len(s) < 20:
        return "c"

    x = np.arange(len(s), dtype=float)
    y = s.to_numpy(dtype=float)
    corr = np.corrcoef(x, y)[0, 1]
    if np.isnan(corr):
        return "c"
    return "ct" if abs(corr) > 0.6 else "c"


def run_stl(
    series: pd.Series,
    period: int = 12,
    log_transform: bool = True,
    robust: bool = True,
):
    """Apply STL decomposition with optional log-transform."""
    s = _validate_series(series, require_positive=log_transform)

    if len(s) < 2 * period:
        raise ValueError(f"series is too short for STL; need at least {2 * period} observations.")

    if log_transform:
        s = np.log(s)

    stl = STL(s, period=period, robust=robust)
    return stl.fit()


def test_stationarity(series: pd.Series, alpha: float = 0.05) -> dict[str, Any]:
    """Run ADF and KPSS tests and return a 2x2 verdict."""
    s = _validate_series(series, require_positive=False)

    if len(s) < 20:
        raise ValueError("series is too short for reliable stationarity testing.")

    regression = _infer_stationarity_regression(s)

    adf_stat, adf_p, _, _, _, _ = adfuller(s, regression=regression)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        kpss_stat, kpss_p, _, _ = kpss(s, regression=regression, nlags="auto")

    adf_reject = adf_p < alpha
    kpss_reject = kpss_p < alpha

    if (not adf_reject) and kpss_reject:
        verdict = "non-stationary"
    elif adf_reject and (not kpss_reject):
        verdict = "stationary"
    else:
        verdict = "mixed"

    return {
        "adf_stat": float(adf_stat),
        "adf_p": float(adf_p),
        "kpss_stat": float(kpss_stat),
        "kpss_p": float(kpss_p),
        "verdict": verdict,
        "regression": regression,
    }


def detect_breaks(series: pd.Series, pen: float = 10) -> list[pd.Timestamp]:
    """Detect structural breaks using PELT."""
    if rpt is None:
        raise ImportError("ruptures is required for detect_breaks(). Install with: pip install ruptures")

    s = _validate_series(series, require_positive=False)
    signal = s.to_numpy(dtype=float).reshape(-1, 1)

    algo = rpt.Pelt(model="l2").fit(signal)
    break_idx = algo.predict(pen=pen)
    break_idx = [idx for idx in break_idx if idx < len(s)]

    return [pd.Timestamp(s.index[idx]) for idx in break_idx]
