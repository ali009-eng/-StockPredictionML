import datetime
import joblib
import os
from sklearn.linear_model import LinearRegression
import numpy as np

# Optional: Use real data if yfinance is available
try:
    import yfinance as yf
    use_real_data = True
except ImportError:
    print("⚠️ yfinance not installed. Using synthetic data.")
    use_real_data = False

STOCKS = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"]

def date_to_ordinal(dates):
    return np.array([d.toordinal() for d in dates]).reshape(-1, 1)

def train_model_for(stock):
    print(f"📊 Training model for {stock}...")

    if use_real_data:
        data = yf.download(stock, period="90d")
        data = data.reset_index()
        dates = [d.date() for d in data['Date']]
        prices = data['Close'].values
    else:
        today = datetime.date.today()
        dates = [today - datetime.timedelta(days=i) for i in range(90)]
        dates.reverse()
        prices = np.linspace(100, 200, 90) + np.random.normal(0, 5, 90)

    X = date_to_ordinal(dates)
    y = prices

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, f"{stock}_model.pkl")
    print(f"✅ Saved model as {stock}_model.pkl")

if __name__ == "__main__":
    for stock in STOCKS:
        train_model_for(stock)
