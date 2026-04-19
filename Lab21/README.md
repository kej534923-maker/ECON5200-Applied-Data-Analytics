# Time Series Forecasting — ARIMA, GARCH & Bootstrap

## Objective

Develop a robust, production-grade time series forecasting pipeline that addresses non-stationarity, seasonality, and volatility clustering, while incorporating statistically sound uncertainty quantification methods.

## Methodology

* Diagnosed a flawed ARIMA pipeline by identifying key specification errors, including failure to difference a non-stationary CPI series, omission of seasonal dynamics, and lack of residual diagnostics.
* Reconstructed the model using a SARIMA framework with appropriate differencing and seasonal components (monthly frequency), ensuring statistical validity.
* Conducted residual diagnostics using the Ljung–Box test to confirm absence of autocorrelation and validate model adequacy prior to forecasting.
* Modeled financial market volatility by fitting a GARCH(1,1) process to S&P 500 daily log returns, capturing volatility clustering and persistence.
* Developed a reusable evaluation module (`forecast_evaluation.py`) featuring:

  * **Mean Absolute Scaled Error (MASE)** for scale-free forecast accuracy comparison
  * **Expanding-window backtesting** to simulate real-world forecasting performance over time
* Implemented block bootstrap techniques to generate distribution-free forecast intervals, preserving residual autocorrelation and heteroskedasticity structures.

## Key Findings

* Correct model specification (SARIMA with seasonal differencing) significantly improved forecast reliability, eliminating residual autocorrelation detected in the initial ARIMA setup.
* Ljung–Box diagnostics confirmed that the final SARIMA residuals behave approximately as white noise, validating model assumptions.
* GARCH(1,1) estimation revealed strong volatility persistence in S&P 500 returns, with α + β ≈ **[0.983]**, implying a shock half-life of approximately **[40] days**.
* Block bootstrap intervals provided wider and more realistic uncertainty bounds compared to standard Gaussian intervals, particularly in the presence of volatility clustering.
* The modular evaluation framework enables scalable and reproducible model comparison across different time series applications.

---
