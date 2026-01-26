# 📊 The Cost of Living Crisis: A Data-Driven Analysis

## 🔍 The Problem: Why the “Average” CPI Fails Students

Official inflation statistics, such as the U.S. Consumer Price Index (CPI), are designed to reflect the spending patterns of the *average* household. However, this aggregation masks substantial heterogeneity across regions and demographic groups.

For students, essential expenses like **tuition, rent, and food away from home** account for a much larger share of their budget than in the official CPI basket. As a result, the headline CPI may significantly **understate the inflation actually experienced by students**, particularly in high-cost metropolitan areas such as Boston.

This project investigates whether students face a systematically higher cost-of-living increase than what national inflation statistics suggest.

---

## 🧠 Methodology: Python, APIs, and Index Theory

I constructed a custom, student-specific inflation index using the following approach:

* **Data Sources**

  * Federal Reserve Economic Data (FRED) API
  * National CPI (CPI-U)
  * Regional CPI for Boston-Cambridge-Newton
  * CPI subcomponents for tuition, rent, streaming services, and food away from home

* **Index Construction**

  * All series are **re-indexed to a common base year (2016 = 100)** to eliminate scale distortions caused by differing CPI base years.
  * A **student-weighted price index (“Student SPI”)** is constructed using a Laspeyres-style framework, reflecting realistic student expenditure shares (e.g., higher weights on tuition and rent).

* **Visualization & Analysis**

  * National CPI, Boston CPI, and Student SPI are plotted together to compare **national averages, regional inflation, and demographic-specific inflation**.
  * Special attention is paid to common data literacy pitfalls such as truncated axes and misleading chart types.

---

## 📈 Key Findings

* **Students experience materially higher inflation than the national average.**
  Since 2016, the Student SPI has diverged from the official CPI by approximately **[2.2]%**, indicating a substantially faster increase in student living costs.

* **Regional effects amplify inflation pressure.**
  Boston’s regional CPI consistently tracks above the national CPI, reflecting elevated housing and service costs in major urban centers.

* **Aggregation hides inequality.**
  While the national CPI suggests moderate inflation, student-weighted costs rise much faster, demonstrating how “average” statistics can obscure lived economic reality.

---

## 💡 Why This Matters

This analysis highlights a broader issue in economic measurement: **who the index is designed for matters**. Policymakers, universities, and employers relying solely on headline CPI may underestimate the financial strain faced by students and young workers, especially in high-cost cities.

By combining API-driven data collection, index theory, and transparent visualization, this project demonstrates how tailored economic indicators can reveal disparities hidden by national averages.

---

## 🛠️ Tools & Skills Demonstrated

* Python (pandas, matplotlib)
* API integration (FRED)
* Index construction & normalization
* Data visualization and data-ethics literacy
* Economic reasoning and applied macroeconomic analysis

---

📌 *This project is intended as a portfolio demonstration of applied data science and economic analysis, emphasizing both technical rigor and clear communication.*
