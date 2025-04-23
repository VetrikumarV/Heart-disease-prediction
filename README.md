
# Heart Disease Prediction App

This is a simple web app built using Streamlit to predict the likelihood of heart disease based on user inputs.

## 🔗 Live Demo
Access the live app here: [Heart Disease Predictor](https://heart-disease-prediction-brst58ac9unegxysny6vep.streamlit.app/)

## 💻 How to Run Locally

1. **Clone or Download this repository**

2. **Install required packages**:
```
pip install -r requirements.txt
```

3. **Add your `model.pkl` file** to the same folder as `app.py`. This should be a trained scikit-learn model.

4. **Run the Streamlit app**:
```
streamlit run app.py
```

## 🧾 Inputs Used for Prediction
- Age
- Sex
- Chest Pain Type (TA, ATA, NAP, ASY)
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Resting ECG Results
- Maximum Heart Rate Achieved
- Exercise Induced Angina
- ST Depression (Oldpeak)
- Slope of ST Segment

## 🧠 Model
Make sure the model was trained using the same features and preprocessing format. The model should be serialized as `model.pkl` using `pickle` or `joblib`.

---

Made with ❤️ using Streamlit.
