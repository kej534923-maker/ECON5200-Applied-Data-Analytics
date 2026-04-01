# The Architecture of Dimensionality: Hedonic Pricing & the FWL Theorem

## Objective
Implement and analyze a multivariate hedonic pricing model to examine how property characteristics influence housing prices while formally demonstrating the Frisch–Waugh–Lovell (FWL) theorem as the algorithmic foundation of ceteris paribus estimation in linear regression.

## Methodology
- Constructed a **hedonic pricing regression** using California real estate data to estimate the relationship between housing prices and key structural and locational characteristics.
- Estimated a **naïve OLS specification** relating `Sale_Price` solely to `Property_Age` in order to identify potential omitted variable bias (OVB).
- Expanded the specification into a **multivariate OLS model** including `Distance_to_Tech_Hub`, capturing locational economic effects associated with proximity to technology employment centers.
- Applied the **Frisch–Waugh–Lovell (FWL) theorem** to manually replicate the multivariate coefficient:
  - Regressed `Sale_Price` on `Distance_to_Tech_Hub` and extracted residuals to remove the influence of tech proximity from the dependent variable.
  - Regressed `Property_Age` on `Distance_to_Tech_Hub` and extracted residuals to remove shared variance between age and location.
  - Regressed the resulting residualized price on residualized age to isolate the **pure partial effect** of property age.
- Verified that the coefficient from the residual-on-residual regression exactly matched the coefficient from the multivariate OLS model, confirming the theoretical identity described by the FWL theorem.

## Key Findings
- The naïve model produced **severe omitted variable bias**, incorrectly attributing price variation associated with technology hub proximity to the physical age of the property.
- Once proximity to technology centers was included in the multivariate model, the estimated contribution of property age changed substantially, revealing that a significant portion of the original relationship was driven by **locational economic effects rather than structural characteristics**.
- The manual implementation of the **FWL theorem successfully decomposed shared covariance**, isolating the independent contribution of property age after controlling for tech proximity.
- The resulting coefficient matched the multivariate OLS estimate exactly, empirically demonstrating that linear regression operationalizes **ceteris paribus conditions through residualization and orthogonalization of regressors**.

This project illustrates how multivariate econometric models correct structural misattribution caused by omitted variables and highlights the geometric and algorithmic foundations of causal interpretation in linear regression.
