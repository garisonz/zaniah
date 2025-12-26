# zaniah
Zaniah is a web application that leverages real-time stock data, news/social sentiment analysis, and machine learning predictions to understand markets and potential price movements.

## ✨ Features

- **Real-time & Historical Stock Data** — Prices, volume, candlesticks
- **Multimodal Sentiment Analysis** — News headlines, earnings tone, social buzz via FinBERT & Hugging Face Transformers
- **Machine Learning Signals** — XGBoost/LightGBM ensembles + time-series forecasting
- **Backtesting Engine** — Strategy evaluation with Sharpe ratio, max drawdown, etc. (powered by vectorbt)
- **Economic Indicators Dashboard** — Macro nowcasting with alternative proxies
- **Interactive Charts** — Beautiful Plotly visualizations (candlesticks, sentiment gauges, heatmaps)
- **One-Click Deployment** — Free hosting on Streamlit Community Cloud

## 🛠 Tech Stack

Frontend * Streamlit [![Streamlit](https://img.shields.io/badge/Streamlit-1.38+-red?style=flat&logo=streamlit)](https://streamlit.io/) |
Data Sources * yfinance polygon.io
Data Handling * pandas, NumPy
NLP / Sentiment * Hugging Face  
Modeling * scikit-learn PyTorch
Backtesting * vectorbt
Visualization * Plotly
Portfolio Tools * PyPortfolioOpt

## 🚀 Quick Start (Local)
