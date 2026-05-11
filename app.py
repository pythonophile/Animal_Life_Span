import streamlit as st
import pandas as pd
import pickle
import numpy as np

# --- STEP 1: LOAD THE SAVED MODELS ---
try:
    with open('linear_model.pkl', 'rb') as f:
        linear_model = pickle.load(f)
    
    with open('poly_model.pkl', 'rb') as f:
        poly_model = pickle.load(f)
        
    with open('poly_converter.pkl', 'rb') as f:
        poly_converter = pickle.load(f)
except FileNotFoundError:
    st.error("Model files not found! Make sure .pkl files are in the same folder.")

# --- STEP 2: DESIGN THE INTERFACE ---
st.set_page_config(page_title="Animal Lifespan Predictor", layout="centered")

st.title("🐾 Animal Lifespan Predictor")
st.write("Enter the characteristics of an animal to predict how long it might live.")

# Create input boxes for the user
speed = st.number_input("Animal Speed (km/h):", min_value=0.0, value=20.0)
weight = st.number_input("Animal Weight (kg):", min_value=0.0, value=50.0)

# Selection for which model to use
model_type = st.radio("Select Prediction Model:", ("Linear Regression", "Polynomial Regression"))

# --- STEP 3: PREDICTION LOGIC ---
if st.button("Predict Lifespan"):
    # Prepare the input data
    user_input = np.array([[speed, weight]])
    
    if model_type == "Linear Regression":
        prediction = linear_model.predict(user_input)
    else:
        # For polynomial, we must transform the input first
        input_poly = poly_converter.transform(user_input)
        prediction = poly_model.predict(input_poly)
    
    # Display the result
    st.success(f"The estimated lifespan is **{prediction[0]:.2f} years**.")

# --- STEP 4: FOOTER ---
st.info("Note: This model is based on historical animal data trends.")