# Copy and paste the following in a text editor. Script to create interface (ie Streamlit app) for the Machine Learning 

import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
model = joblib.load('medal_model.pkl')

st.title("Olympic Medal Prediction")
st.write("Enter athlete information to predict medal probability")

# Create input fields (simplified example, consistent with feature names from training)
age = st.number_input("Age", min_value=10, max_value=80, value=25)
height = st.number_input("Height (cm)", min_value=100, max_value=250, value=175)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
bmi = weight / ((height/100) ** 2)

sex = st.selectbox("Sex", ["M", "F"])
sport = st.text_input("SportKey", "Athletics")
noc = st.text_input("NOCKey", "USA")

if st.button("Predict"):
    # Construct a single-row DataFrame, column names must match training
    input_df = pd.DataFrame([[age, height, weight, bmi, sex, sport, noc]],
                            columns=["Age", "Height", "Weight", "BMI", "Sex", "SportKey", "NOCKey"])
    
    # Note: The model pipeline from training already includes preprocessing (imputation, encoding, scaling), so you can predict directly
    prob = model.predict_proba(input_df)[0][1]
    st.success(f"Medal probability: {prob:.2%}")