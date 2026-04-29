import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("outputs/model.pkl")

st.title("Employee Performance Predictor")

age = st.slider("Age", 20, 60)
env = st.slider("Environment Satisfaction", 1, 4)
work = st.slider("Work-Life Balance", 1, 4)

if st.button("Predict"):
    data = np.array([[age, env, work]])
    result = model.predict(data)
    st.success(f"Performance Rating: {result[0]}")
