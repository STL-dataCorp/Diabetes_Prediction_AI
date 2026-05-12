import streamlit as st
import requests

# Configuration de la page
st.set_page_config(
    page_title="Prédiction Diabète",
    page_icon="🩺",
    layout="centered"
)

# Titre et description
st.title("🩺 Prédiction du Diabète")
st.markdown("Remplis les informations du patient pour obtenir une prédiction.")
st.divider()

# Formulaire de saisie
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Grossesses (Pregnancies)", min_value=0, max_value=20, value=2)
    glucose = st.number_input("Glucose", min_value=0, max_value=300, value=120)
    blood_pressure = st.number_input("Pression sanguine (BloodPressure)", min_value=0, max_value=200, value=70)
    skin_thickness = st.number_input("Épaisseur peau (SkinThickness)", min_value=0, max_value=100, value=20)

with col2:
    insulin = st.number_input("Insuline (Insulin)", min_value=0, max_value=900, value=79)
    bmi = st.number_input("IMC (BMI)", min_value=0.0, max_value=70.0, value=25.0, step=0.1)
    dpf = st.number_input("Diabète Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, step=0.01)
    age = st.number_input("Âge (Age)", min_value=1, max_value=120, value=33)

st.divider()

# Bouton de prédiction
if st.button("🔍 Lancer la prédiction", use_container_width=True):

    # Préparer les données
    patient_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }

    try:
        # Appel à l'API FastAPI
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=patient_data
        )

        result = response.json()

        st.divider()

        # Afficher le résultat
        if result["prediction"] == 1:
            st.error(f"⚠️ Résultat : **{result['resultat']}**")
        else:
            st.success(f"✅ Résultat : **{result['resultat']}**")

        # Afficher la probabilité
        st.metric(
            label="Probabilité de diabète",
            value=f"{result['probabilite_diabete']} %"
        )

    except Exception as e:
        st.warning("⚠️ Impossible de contacter l'API. Vérifie que FastAPI est bien lancé.")