## 📉 The Illusion of Growth & The Composition Effect  
**Deflating History with FRED**

### 🎯 Objective
The goal of this project is to analyze long-run U.S. wage dynamics by correcting for inflation and statistical distortions.  
Using live macroeconomic data from the Federal Reserve, I examine whether apparent wage growth reflects genuine improvements in workers’ purchasing power—or merely a *money illusion* driven by nominal values and compositional changes in the labor force.

---

### 🧪 Methodology

This project implements a fully reproducible Python data pipeline built around live economic data ingestion.

1. **API-Based Data Collection**  
   - Retrieved nominal wage data (Average Hourly Earnings, *AHETPI*) and consumer price inflation (CPI) using the Federal Reserve API.
   - Constructed real wage series by deflating nominal wages to constant dollars.

2. **Anomaly Detection: The Pandemic Spike**  
   - Identified a sharp increase in real wages during 2020 that conflicted with underlying economic conditions.
   - Flagged this divergence as a potential statistical artifact rather than a true labor market improvement.

3. **Composition Effect Correction**  
   - Retrieved the Employment Cost Index (ECI) to control for labor-force composition changes.
   - Demonstrated that the 2020 “wage boom” was driven by the exit of low-wage workers during the pandemic, artificially inflating average wages.

This correction allows for a cleaner interpretation of wage dynamics that isolates true compensation trends from compositional bias.

---

### 🔍 Key Findings: The Pandemic Paradox

- **The Money Illusion:**  
  Over the past five decades, nominal wages have risen steadily, but real wages—after adjusting for inflation—remain largely flat, revealing persistent wage stagnation.

- **The Pandemic Paradox:**  
  The apparent surge in real wages during 2020 was not caused by increased labor demand or productivity gains. Instead, it was a statistical illusion driven by labor-force contraction among lower-wage workers.

- **Economic Insight:**  
  This project highlights the importance of combining economic theory with data diagnostics: without correcting for composition effects, headline wage statistics can be deeply misleading.

---

### 🛠️ Tools & Libraries
- Python  
- `fredapi`  
- `pandas`  
- `matplotlib`
