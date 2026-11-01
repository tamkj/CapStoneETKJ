# Copy and paste the following in a text editor. Script to create interface (ie Streamlit app) for the Machine Learning 

import streamlit as st
import pandas as pd
import joblib

# ---------- Load model ----------
model = joblib.load("medal_model.pkl")

# ---------- Pull dropdown options from the fitted encoder ----------
# cat_features order in training: ["Sex", "SportKey", "NOCKey"]
# so categories_[0]=Sex, categories_[1]=SportKey, categories_[2]=NOCKey
encoder = model.named_steps["prep"].named_transformers_["cat"].named_steps["onehot"]
sex_options   = encoder.categories_[0].tolist()
sport_options = encoder.categories_[1].tolist()
noc_options   = encoder.categories_[2].tolist()

# ---------- Page ----------
st.set_page_config(page_title="Olympic Medal Predictor", page_icon="🏅")
st.title("🏅 Olympic Medal Prediction")
st.write("Enter athlete and event information to estimate the probability of winning a medal.")

# ---------- Inputs ----------
col1, col2 = st.columns(2)

with col1:
    age    = st.number_input("Age", min_value=10, max_value=80, value=25, step=1)
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=175, step=1)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70, step=1)
    sex    = st.selectbox("Sex", sex_options)

with col2:
    sport = st.selectbox("Sport", sport_options)
    noc   = st.selectbox("NOC (Country)", noc_options)

bmi = weight / ((height / 100) ** 2)
st.caption(f"Computed BMI: **{bmi:.1f}**")

# ---------- Predict ----------
if st.button("Predict medal probability"):
    input_df = pd.DataFrame(
        [[age, height, weight, bmi, sex, sport, noc]],
        columns=["Age", "Height", "Weight", "BMI", "Sex", "SportKey", "NOCKey"],
    )

    prob = float(model.predict_proba(input_df)[0, 1])
    pred = "Medal" if prob >= 0.5 else "No medal"

    st.success(f"**Predicted: {pred}** — probability of medal: **{prob:.2%}**")
    st.progress(min(max(prob, 0.0), 1.0))

    with st.expander("See input sent to model"):
        st.dataframe(input_df)