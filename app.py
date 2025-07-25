from flask import Flask, request, render_template_string
import joblib
import datetime
import os

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Stock Price Predictor</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: #f8f9fa;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .card {
      padding: 30px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.1);
      border-radius: 16px;
      background: white;
      max-width: 450px;
      width: 100%;
    }
  </style>
</head>
<body>
  <div class="card">
    <h2 class="mb-4 text-center"> Stock Price Predictor</h2>
    <form method="post">
      <div class="mb-3">
        <label for="stock" class="form-label">Select Stock</label>
        <select name="stock" class="form-select" id="stock" required>
          {% for s in stocks %}
          <option value="{{ s }}">{{ s }}</option>
          {% endfor %}
        </select>
      </div>
      <div class="mb-3">
        <label for="days" class="form-label">Days into Future (0–30)</label>
        <input type="number" class="form-control" id="days" name="days" value="1" min="0" max="30" required>
      </div>
      <button type="submit" class="btn btn-primary w-100">Predict</button>
    </form>
    {% if prediction %}
    <div class="alert alert-success mt-4 text-center" role="alert">
       Predicted Price: <strong>${{ prediction }}</strong>
    </div>
    {% elif error %}
    <div class="alert alert-danger mt-4 text-center" role="alert">
       {{ error }}
    </div>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None
    stocks = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"]
    
    if request.method == "POST":
        stock = request.form["stock"]
        days = int(request.form["days"])
        model_path = f"{stock}_model.pkl"
        
        if not os.path.exists(model_path):
            error = f"Model file '{model_path}' not found."
        else:
            try:
                model = joblib.load(model_path)
                future_date = datetime.date.today() + datetime.timedelta(days=days)
                ordinal = future_date.toordinal()
                predicted = model.predict([[ordinal]])[0]
                prediction = round(float(predicted), 2)  #  Convert to float, then round
            except Exception as e:
                error = f"Prediction failed: {e}"
    
    return render_template_string(TEMPLATE, prediction=prediction, error=error, stocks=stocks)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
