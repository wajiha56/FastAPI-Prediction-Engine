from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(title="Wajiha's AI Engine API")


# Home route
@app.get("/")
def home():
    return {
        "message": "Welcome to the Wajiha AI Server! System is 100% Online."
    }


# Prediction endpoint
@app.get("/predict")
def predict_sales(age: int, minutes_on_site: int):
    """
    Simple AI rule-based prediction
    """

    if age > 25 and minutes_on_site > 10:
        prediction = "Customer WILL BUY ✅"
    else:
        prediction = "Customer WILL NOT BUY ❌"

    return {
        "customer_age": age,
        "time_spent": minutes_on_site,
        "ai_prediction": prediction
    }