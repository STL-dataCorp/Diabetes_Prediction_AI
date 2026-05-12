# 🩺 Diabetes Prediction AI

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red)
![Scikit-learn](https://img.shields.io/badge/ScikitLearn-1.0+-orange)
![Render](https://img.shields.io/badge/Deployed-Render-purple)

Système intelligent de prédiction du diabète basé sur le Machine Learning.
Ce projet permet, à partir de données médicales d'un patient, de prédire
avec un modèle entraîné si ce patient est susceptible d'être diabétique ou non.

---

## 📌 Contexte du projet

Le diabète est l'une des maladies chroniques les plus répandues dans le monde.
Un diagnostic précoce est essentiel pour améliorer la qualité de vie des patients.

Ce projet exploite le dataset **Pima Indians Diabetes Database** (UCI / Kaggle),
qui contient des données médicales de femmes âgées de 21 ans et plus,
afin d'entraîner un modèle de classification capable de prédire
la présence ou l'absence de diabète.

---

## 🎯 Objectif

Construire un pipeline complet de Machine Learning comprenant :

- l'analyse et le nettoyage des données ;
- l'entraînement d'un modèle de classification supervisée ;
- l'exposition du modèle via une API REST (FastAPI) ;
- une interface utilisateur interactive (Streamlit) ;
- un déploiement en ligne accessible publiquement (Render).

---

## 📊 Dataset

- **Source** : [Pima Indians Diabetes Database — Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Taille** : 2269 entrées, 9 colonnes
- **Cible** : colonne `Outcome` (0 = Non diabétique, 1 = Diabétique)

### Variables du dataset

| Variable | Description |
|---|---|
| Pregnancies | Nombre de grossesses |
| Glucose | Concentration en glucose (mg/dL) |
| BloodPressure | Pression artérielle diastolique (mm Hg) |
| SkinThickness | Épaisseur du pli cutané tricipital (mm) |
| Insulin | Taux d'insuline sérique (µU/mL) |
| BMI | Indice de masse corporelle (kg/m²) |
| DiabetesPedigreeFunction | Score héréditaire du diabète |
| Age | Âge du patient (années) |
| Outcome | Résultat : 0 = sain, 1 = diabétique |

---

## 🤖 Modèle de Machine Learning

- **Algorithme** : Random Forest Classifier
- **Librairie** : Scikit-learn
- **Précision obtenue** : ~80% (accuracy sur le jeu de test)

### Étapes du pipeline ML

1. Chargement du dataset
2. Remplacement des zéros biologiquement impossibles par la médiane
3. Séparation features / target
4. Split train/test (80% / 20%)
5. Entraînement du Random Forest (100 arbres)
6. Évaluation : accuracy, matrice de confusion, rapport de classification
7. Sauvegarde du modèle (`diabetes_model.pkl`)

---

## 🏗️ Architecture du projet

diabetes_prediction_ai/
│
├── data/
│   └── diabetes.csv          # Dataset brut
│
├── notebooks/
│   └── analysis.ipynb        # Analyse, visualisation, entraînement
│
├── model/
│   └── diabetes_model.pkl    # Modèle sauvegardé
│
├── main.py                   # API FastAPI
├── streamlit_app.py          # Interface utilisateur Streamlit
├── requirements.txt          # Dépendances Python
├── lien.txt                  # Liens de déploiement
└── README.md                 # Documentation du projet

---

## 🚀 Lancer le projet localement

### 1. Cloner le repository

```bash
git clone https://github.com/STL-dataCorp/diabetes-prediction-ai.git
cd diabetes-prediction-ai
```

### 2. Créer et activer l'environnement virtuel

```bash
python -m venv venv
```

Windows :
```bash
venv\Scripts\activate
```

Linux / Mac :
```bash
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l'API FastAPI

```bash
uvicorn main:app --reload
```

API disponible sur :
http://127.0.0.1:8000

Documentation Swagger :
http://127.0.0.1:8000/docs

### 5. Lancer l'interface Streamlit

Dans un second terminal :

```bash
streamlit run streamlit_app.py
```

Interface disponible sur :
http://localhost:8501

---

## 🌐 Déploiement en ligne

| Service | Lien |
|---|---|
| API FastAPI (Render) | https://diabetes-prediction-ai-zaay.onrender.com/ |
| Documentation Swagger | https://diabetes-prediction-ai-zaay.onrender.com//docs |
| Code source (GitHub) | https://github.com/STL-dataCorp/Diabetes_Prediction_AI|
 
---

## 🔌 Utilisation de l'API

### Endpoint de prédiction
POST /predict

### Exemple de requête

```json
{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 79,
  "BMI": 25.0,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 33
}
```

### Exemple de réponse

```json
{
  "prediction": 0,
  "resultat": "Non diabétique",
  "probabilite_diabete": 18.5
}
```

---

## 🧪 Cas de test

| Profil | Glucose | BMI | Age | Résultat attendu |
|---|---|---|---|---|
| Jeune femme saine | 85 | 26.6 | 24 | Non diabétique |
| Femme obèse âgée | 183 | 23.3 | 52 | Diabétique |
| Profil à risque élevé | 166 | 25.8 | 51 | Diabétique |
| Cas limite | 128 | 28.5 | 38 | Variable |

---

## 🛠️ Technologies utilisées

| Technologie | Rôle |
|---|---|
| Python 3.11 | Langage principal |
| Pandas / NumPy | Manipulation des données |
| Matplotlib / Seaborn | Visualisation |
| Scikit-learn | Entraînement du modèle |
| FastAPI | API REST |
| Uvicorn | Serveur ASGI |
| Streamlit | Interface utilisateur |
| Joblib | Sauvegarde du modèle |
| Render | Déploiement cloud |
| GitHub | Versioning du code |

---

## 👤 Auteur

**GEUTUI TCHEUTOU SAINT LOIC**
Étudiant en Data Science / Intelligence Artificielle

