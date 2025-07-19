import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load trained model
model = joblib.load("salary_boosted_model.joblib")

st.set_page_config(page_title="Salary Predictor", page_icon="💰", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>💼 Employee Salary Predictor</h1>", unsafe_allow_html=True)
st.write("Predict an employee's salary based on role, education, experience, and more!")

# Input Form
with st.form("salary_form"):
    st.subheader("📝 Enter Employee Details")

    col1, col2 = st.columns(2)

    with col1:
        education = st.selectbox("🎓 Education Level", ["Master","High School", "Bachelor", "PhD"])
        job_title = st.selectbox("👔 Job Title", ["Engineer","Manager", "Analyst", "Director"])
        gender = st.radio("⚧️ Gender", ["Male", "Female"], horizontal=True)

    with col2:
        experience = st.slider("💼 Years of Experience", 0, 40, 5)
        age = st.slider("📅 Age", 18, 65, 30)
        location = st.selectbox("📍 Work Location", ["Urban", "Suburban", "Rural"])

    submitted = st.form_submit_button("🔍 Predict Salary")

# Predict Salary
if submitted:
    input_data = {
        'Education': [education],
        'Experience': [experience],
        'Location': [location],
        'Job_Title': [job_title],
        'Age': [age],
        'Gender': [gender]
    }

    input_df = pd.DataFrame(input_data)
    prediction = model.predict(input_df)[0]

    st.success(f"💸 Estimated Monthly Salary: ₹ {prediction:,.2f}")
 
