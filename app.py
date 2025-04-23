import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("Heart Disease Prediction")

# Input fields for user to enter data
age = st.number_input("Age", min_value=0, max_value=100, value=30)
sex = st.selectbox("Sex", ["Female", "Male"])  # 0: Female, 1: Male
chest_pain_type = st.selectbox("Chest Pain Type", ["TA", "ATA", "NAP", "ASY"]) 
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, value=120)
cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=0, value=200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", ["No", "Yes"])  # 0: No, 1: Yes
resting_ecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST", "LVH"])
max_hr = st.number_input("Maximum Heart Rate Achieved", min_value=0, value=150)
exercise_angina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])  # 0: No, 1: Yes
oldpeak = st.number_input("ST depression induced by exercise relative to rest", min_value=0.0, value=1.0)
st_slope = st.selectbox("The slope of the peak exercise ST segment", ["Up", "Flat", "Down"])

# Preprocess input data
sex = 1 if sex == "Male" else 0
chest_pain_type = ["TA", "ATA", "NAP", "ASY"].index(chest_pain_type)
fasting_bs = 1 if fasting_bs == "Yes" else 0
resting_ecg = ["Normal", "ST", "LVH"].index(resting_ecg)
exercise_angina = 1 if exercise_angina == "Yes" else 0
st_slope = ["Up", "Flat", "Down"].index(st_slope)

# Create input data array
input_data = np.array([age, sex, chest_pain_type, resting_bp, cholesterol, fasting_bs,
                       resting_ecg, max_hr, exercise_angina, oldpeak, st_slope]).reshape(1, -1)

# Make prediction
if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("The Patient has Heart Disease, please consult the Doctor") 
    else:
        st.success("The Patient is Normal")