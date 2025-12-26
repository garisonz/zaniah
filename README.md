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

## 🛠 Tech Stack

| Layer              | Technology                                      | Badge |
|--------------------|-------------------------------------------------|-------|
| Dashboard         | Streamlit                                       | [![Streamlit](https://img.shields.io/badge/Streamlit-1.38+-red?style=flat&logo=streamlit)](https://streamlit.io/) |
| Data Sources      | yfinance (free prototyping)<br>Polygon.io / Finnhub (real-time & production) | [![yfinance](https://img.shields.io/badge/yfinance-latest-blue?style=flat)](https://pypi.org/project/yfinance/)<br>[![Polygon](https://img.shields.io/badge/Polygon.io-real--time-green?style=flat)](https://polygon.io/) [![Finnhub](https://img.shields.io/badge/Finnhub-real--time-teal?style=flat)](https://finnhub.io/) |
| Data Handling     | pandas, NumPy                                   | [![pandas](https://img.shields.io/badge/pandas-latest-blue?style=flat&logo=pandas)](https://pandas.pydata.org/) |
| NLP / Sentiment   | Hugging Face Transformers (FinBERT)             | [![Transformers](https://img.shields.io/badge/Transformers-HuggingFace-orange?style=flat&logo=huggingface)](https://huggingface.co/) |
| Modeling          | scikit-learn, XGBoost, LightGBM, PyTorch        | [![scikit-learn](https://img.shields.io/badge/scikit--learn-latest-orange?style=flat)](https://scikit-learn.org/)<br>[![XGBoost](https://img.shields.io/badge/XGBoost-latest-green?style=flat)](https://xgboost.readthedocs.io/) |
| Backtesting       | vectorbt                                        | [![vectorbt](https://img.shields.io/badge/vectorbt-latest-blue?style=flat)](https://vectorbt.dev/) |
| Visualization     | Plotly                                          | [![Plotly](https://img.shields.io/badge/Plotly-interactive-blue?style=flat&logo=plotly)](https://plotly.com/python/) |
| Portfolio Tools   | PyPortfolioOpt, CVXPY                           | [![PyPortfolioOpt](https://img.shields.io/badge/PyPortfolioOpt-latest-teal?style=flat)](https://pyportfolioopt.readthedocs.io/)<br>[![CVXPY](https://img.shields.io/badge/CVXPY-optimization-green?style=flat)](https://www.cvxpy.org/) |

## 🚀 Quick Start (Local)
