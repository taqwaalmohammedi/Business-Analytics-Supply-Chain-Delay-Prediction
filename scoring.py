import joblib
import pandas as pd

# Load model
def load_model():
    return joblib.load('model.joblib')

# Prediction function
def predict(data):
    model = load_model()
    return model.predict(data)

# Test with sample data
if __name__ == "__main__":
    print("Scoring script is ready")