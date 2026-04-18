## Part 1: Diagnose — STL Decomposition Bug

### What was wrong

STL was applied directly to the raw retail sales series (`RSXFSN`), which assumes an **additive decomposition**. However, the data exhibits **multiplicative seasonality**, where seasonal fluctuations grow with the level of the series.

---

### Why this happens

In multiplicative processes, the seasonal component scales with the trend:

\[
y_t = T_t \times S_t \times E_t
\]

As the series grows over time, the absolute magnitude of seasonal fluctuations also increases. Applying additive STL:

\[
y_t = T_t + S_t + E_t
\]

forces STL to treat seasonal effects as constant, which leads to an apparent **increase in seasonal amplitude over time**.

---

### Fix applied

Log-transform the series before applying STL:

```python
log_series = np.log(series)
stl = STL(log_series, period=12, robust=True)
res = stl.fit()
