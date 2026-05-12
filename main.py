from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Charger le modèle
model = joblib.load("diabetes_model.pkl")

# Initialiser l'application
app = FastAPI(
    title="API Prédiction Diabète",
    description="Prédit si un patient est diabétique ou non.",
    version="1.0.0"
)

# Définir la structure des données d'entrée
class PatientData(BaseModel):
    Pregnancies: float
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: float

# Route d'accueil
@app.get("/")
def home():
    return {"message": "API Diabète opérationnelle ✅"}

# Route de prédiction
@app.post("/predict")
def predict(data: PatientData):
    input_data = np.array([[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    result = "Diabétique" if prediction[0] == 1 else "Non diabétique"

    return {
        "prediction": int(prediction[0]),
        "resultat": result,
        "probabilite_diabete": round(float(probability[0][1]) * 100, 2)
    }