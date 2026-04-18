# Time Series Diagnostics & Decomposition Proposal

## Objective

The objective of this project is to develop a robust and interpretable framework for analyzing time series data using a diagnosis-first approach. The project focuses on identifying common pitfalls in time series decomposition, correctly testing for stationarity, and quantifying uncertainty in trend estimation.

## Methodology

This project integrates several econometric and statistical techniques:

- **STL Decomposition**: Applied to economic time series, with a correction for multiplicative structures using log transformation.
- **Stationarity Testing**: Combines Augmented Dickey-Fuller (ADF) and KPSS tests, with careful attention to model specification (constant vs trend).
- **MSTL (Multiple Seasonal Decomposition)**: Used to analyze simulated electricity demand data with both daily and weekly cycles.
- **Structural Break Detection**: Implemented using the PELT algorithm to identify regime changes in macroeconomic time series.
- **Block Bootstrap**: Used to estimate uncertainty in trend extraction while preserving autocorrelation structure.

## Key Challenges

Several methodological challenges were addressed:

- Misapplication of additive decomposition to multiplicative data
- Incorrect ADF specification leading to misleading stationarity conclusions
- Separating multiple seasonal patterns in high-frequency data
- Preserving time dependence in bootstrap resampling

## Expected Outcomes

The project produces:

- A reusable Python module (`decompose.py`) for time series diagnostics
- Visualizations of decomposition, structural breaks, and uncertainty bands
- An improved understanding of how modeling assumptions affect results

## Significance

This work demonstrates how combining econometric theory with practical implementation can lead to more reliable and interpretable time series analysis. It is particularly relevant for macroeconomic data, where trends, structural breaks, and non-stationarity are common.

## Tools and Technologies

- Python (pandas, numpy)
- statsmodels (STL, ADF, KPSS)
- ruptures (PELT algorithm)
- matplotlib / plotly
- fredapi (economic data)
