# Causal ML — DML and Causal Forests for Policy Evaluation

## Objective  
Estimate the causal effect of 401(k) eligibility on household financial assets using modern causal machine learning methods, and evaluate treatment effect heterogeneity to inform policy targeting.

## Methodology  
- Diagnosed and corrected a broken manual Double Machine Learning (DML) implementation by fixing cross-fitting leakage, adding treatment residualization, and applying the correct IV-style estimator  
- Verified correctness on a simulated data-generating process (DGP) by recovering the true ATE  
- Implemented DoubleML (PLR) with Random Forest nuisance models and 5-fold cross-fitting to estimate the average treatment effect (ATE)  
- Conducted sensitivity analysis to assess robustness to unobserved confounding  
- Applied CausalForestDML (EconML) to estimate individual-level Conditional Average Treatment Effects (CATEs)  
- Compared subgroup DML (income quartiles) with Causal Forest outputs to evaluate coarse vs. continuous heterogeneity detection  
- Visualized treatment effect distributions and analyzed subgroup characteristics  

## Key Findings  
- 401(k) eligibility has a positive and statistically significant impact on net financial assets, with an estimated ATE in the range of approximately $7,000–$12,000  
- Sensitivity analysis indicates the result is robust to moderate levels of unobserved confounding, supporting a causal interpretation  
- Subgroup DML reveals differences across income quartiles, but substantial variation remains within each quartile  
- Causal Forest uncovers richer, continuous heterogeneity, showing that treatment effects vary significantly across individuals even within the same income group  
- Overall, Causal Forest provides a more granular understanding of who benefits most, while DML offers a stable and interpretable average policy effect
