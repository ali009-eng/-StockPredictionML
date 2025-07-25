Stock Price Prediction Web App
This project is a machine learning-based web application that predicts the next-day closing price of major stocks (AAPL, AMZN, GOOG, MSFT, TSLA). It uses historical market data and trained regression models for each stock. The app is built using Python, Flask, and scikit-learn, and is exposed to the web using ngrok.

Features
Predicts next-day closing prices for selected stocks.

Separate ML models trained per stock using historical data.

Simple Flask-based REST API.

Deployment via ngrok for easy public access.

 Machine Learning
Data Source: Historical daily stock prices (Open, High, Low, Close, Volume) via yfinance.

Models Used: Scikit-learn regressors (e.g., Linear Regression, Random Forest).

Preprocessing:

Cleaned missing values.

Generated lag features (e.g., yesterday's close).

Train-test split.

Model Storage: Models are saved in .pkl format using joblib or pickle.
