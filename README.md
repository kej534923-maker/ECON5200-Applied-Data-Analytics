# Audit 02: Deconstructing Statistical Lies

## Overview

This audit investigates how statistical framing and data biases can distort conclusions in modern digital analytics, AI detection systems, financial markets, and A/B testing environments. Using simulated experiments and probabilistic reasoning, the project highlights how seemingly “accurate” metrics can mislead decision-makers.

---

## Key Findings

### 1. Latency Skew (Engineering Bias in Experiments)

Even perfectly randomized A/B tests can become invalid when technical issues affect data capture unevenly across groups.
Sample Ratio Mismatch (SRM) testing revealed that small allocation imbalances may arise from logging delays, crashes, or deployment bugs rather than user behavior.
**Takeaway:** Always validate experiment integrity before interpreting performance results.

---

### 2. False Positives & Base Rate Effects

High model accuracy does not guarantee reliable predictions when the underlying event is rare.
Bayesian auditing of an AI plagiarism detector (98% sensitivity/specificity) showed that in low-cheating environments, most flagged cases may still be innocent.
**Takeaway:** Accuracy metrics must be interpreted alongside base rates to avoid systematic false accusations.

---

### 3. Survivorship Bias in Crypto Markets

Simulation of 10,000 token launches using a Pareto distribution demonstrated that a tiny fraction of winners dominate average market capitalization.
Analyzing only surviving tokens drastically inflates perceived performance and understates failure risk.
**Takeaway:** Always include the “graveyard” of failed assets when evaluating investment outcomes.

---

## Methods

* Monte Carlo simulation with heavy-tail distributions
* Bayesian posterior probability auditing
* Chi-Square goodness-of-fit tests for SRM detection
* Comparative distribution visualization (NumPy / Pandas / Matplotlib)

---

## Key Lessons

* Statistical accuracy without context can mislead.
* Engineering artifacts often masquerade as user behavior.
* Ignoring failures produces unrealistic expectations.

**Bottom Line:** Robust analytics requires skepticism, probabilistic thinking, and full-population data—not just convenient samples.
t from Task 4.2.
