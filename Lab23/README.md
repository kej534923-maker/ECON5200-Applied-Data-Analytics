# FedSpeak 2.0 — NLP Pipeline for Central Bank Communications

## Objective

Develop a robust, production-grade NLP pipeline to extract and quantify policy signals from FOMC minutes, and evaluate their predictive power for Federal Reserve rate decisions.

## Methodology

* Diagnosed and corrected a broken NLP pipeline, identifying issues in tokenization, sentiment dictionary selection, and TF-IDF configuration
* Implemented proper preprocessing using `nltk.word_tokenize`, regex-based cleaning, stopword removal, and lemmatization
* Replaced the Harvard General Inquirer dictionary with the Loughran–McDonald financial sentiment lexicon to ensure domain-appropriate sentiment measurement
* Reconstructed TF-IDF features using optimized parameters (`min_df`, `max_df`, and bigrams) to reduce noise and improve signal quality
* Encoded FOMC minutes using sentence-transformers (`all-MiniLM-L6-v2`) to capture semantic and contextual meaning
* Compared TF-IDF and embedding-based representations via clustering (K-Means) and silhouette scores
* Evaluated predictive performance using expanding-window time-series cross-validation and logistic regression
* Built a reusable Python module (`fomc_sentiment.py`) for preprocessing, sentiment scoring, and feature engineering

## Key Findings

* **TF-IDF achieved higher predictive performance**, with an average AUC of **0.82 ± 0.17**, compared to **0.78 ± 0.16** for embeddings
* Results suggest that **sparse, interpretable term-frequency features align strongly with policy-relevant language**, especially in structured institutional text like FOMC minutes
* While embeddings capture richer semantic context, **TF-IDF better isolates recurring policy keywords and signals tied to tightening regimes**
* These findings highlight a trade-off between interpretability and semantic depth, with TF-IDF proving more effective for this specific policy prediction task
