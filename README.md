# 🩺 AI-Powered Diabetes Prediction System

## 📌 Project Overview

The **AI-Powered Diabetes Prediction System** is a Machine Learning-based web application that predicts a patient's diabetes status using health-related indicators. The system analyzes patient data and classifies the individual into one of three categories:

* **0 – No Diabetes**
* **1 – Prediabetes**
* **2 – Diabetes**

The project follows a complete machine learning workflow, including data preprocessing, exploratory data analysis (EDA), model training, model evaluation, model comparison, and deployment using Streamlit.

---

# 🎯 Objectives

* Predict diabetes status using Machine Learning.
* Compare multiple classification algorithms.
* Identify the best-performing model.
* Build an interactive web application for prediction.
* Demonstrate a complete end-to-end ML project suitable for academic presentations.

---

# 📂 Dataset

**Dataset Name**

`diabetes_012_health_indicators_BRFSS2015.csv`

The dataset is based on the Behavioral Risk Factor Surveillance System (BRFSS) 2015 health survey and contains health-related indicators used for diabetes prediction.

### Target Variable

| Value | Meaning     |
| ----- | ----------- |
| 0     | No Diabetes |
| 1     | Prediabetes |
| 2     | Diabetes    |

---

# 📊 Features

The dataset contains the following health indicators:

* HighBP
* HighChol
* CholCheck
* BMI
* Smoker
* Stroke
* HeartDiseaseorAttack
* PhysActivity
* Fruits
* Veggies
* HvyAlcoholConsump
* AnyHealthcare
* NoDocbcCost
* GenHlth
* MentHlth
* PhysHlth
* DiffWalk
* Sex
* Age
* Education
* Income

---

# ⚙️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook

---

# 🤖 Machine Learning Models

The following classification algorithms were trained and compared:

* Logistic Regression
* Decision Tree
* Random Forest
* Extra Trees
* Gradient Boosting
* AdaBoost
* K-Nearest Neighbors (KNN)
* Gaussian Naive Bayes

The best-performing model was selected based on evaluation metrics and saved for deployment.

---

# 📈 Project Workflow

1. Import Libraries
2. Load Dataset
3. Data Exploration
4. Missing Value Check
5. Duplicate Removal
6. Exploratory Data Analysis (EDA)
7. Feature Selection
8. Train-Test Split
9. Feature Scaling
10. Model Training
11. Model Comparison
12. Performance Evaluation
13. Save Best Model
14. Build Streamlit Application
15. Deploy the Application

---

# 📊 Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

---

# 📁 Project Structure

```
Diabetes_Prediction_System/

│── app.py
│── requirements.txt
│── README.md
│
├── data/
│     └── diabetes_012_health_indicators_BRFSS2015.csv
│
├── models/
│     ├── diabetes_model.pkl
│     ├── scaler.pkl
│     └── features.pkl
│
├── notebooks/
│     └── diabetes_prediction.ipynb
│
└── screenshots/
```

---

# 🚀 How to Run

## 1. Clone the Repository

```bash
git clone  https://github.com/shahzada3/Medical-Diabetes

## 2. Navigate to the Project

```bash
cd Diabetes_Prediction_System
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Application

```bash
streamlit run app.py
```

---

# 💻 Application Features

* Interactive user interface
* Patient health data input
* Real-time diabetes prediction
* Prediction confidence score
* Fast and lightweight deployment
* User-friendly design

---

# 📌 Future Enhancements

* Explainable AI (SHAP & LIME)
* XGBoost, LightGBM, and CatBoost models
* Hyperparameter tuning
* FastAPI backend
* React frontend
* Prediction history
* Authentication and user management
* Docker support
* Cloud deployment with CI/CD

---

# 👨‍💻 Author

**Shivansh Vishwakarma**

B.Tech (Artificial Intelligence & Machine Learning)

---

# 📄 License

This project is developed for educational and academic purposes. It may be modified and extended for research, learning, or portfolio use.
