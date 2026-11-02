import streamlit as st
import numpy as np
import joblib

# Load Model
model = joblib.load('model/model.pkl')

# Page Configuration
st.set_page_config(
    page_title="Placement Predictor",
    page_icon="🎓",
    layout="centered"
)

# Heading
st.title("🎓 Student Placement Predictor")

st.write(
    "Predict whether a student will get placed "
    "based on CGPA and IQ."
)

st.divider()

# Input Fields
cgpa = st.number_input(
    "Enter Your CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0,
    step=0.1
)

iq = st.number_input(
    "Enter Your IQ",
    min_value=0,
    max_value=200,
    value=100
)

# Prediction Button
if st.button("Predict Placement"):

    input_data = np.array([[cgpa, iq]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🎉 Congratulations! Student is Likely to be Placed.")
    else:
        st.error("Sorry! Student is Likely Not to be Placed.")