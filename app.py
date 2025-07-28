import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("best_gbr_model.joblib")

st.title("🏡 House Price Estimator")

# User inputs
epc = st.selectbox("EPC Rating", ["A", "B", "C", "D", "E", "F", "G"])
tenure = st.selectbox("Tenure", ["Freehold", "Leasehold"])
property_type = st.selectbox("Property Type", ["Terraced", "Semi-Detached", "Detached", "Flat/Maisonette"])
floor_area = st.number_input("Floor Area (m²)", min_value=10, max_value=1000, value=75)
age = st.number_input("Estimated Property Age", min_value=0, max_value=200, value=50)

# Convert inputs to match model
data = {
    "Floor Area (m2)": [floor_area],
    "lowest property age": [age],
    "Property Type_F": [property_type == "Flat/Maisonette"],
    "Property Type_S": [property_type == "Semi-Detached"],
    "Property Type_T": [property_type == "Terraced"],
    "Tenure_L": [tenure == "Leasehold"],
    "EPC_B": [epc == "B"],
    "EPC_C": [epc == "C"],
    "EPC_D": [epc == "D"],
    "EPC_E": [epc == "E"],
    "EPC_G": [epc == "G"],
}

input_df = pd.DataFrame(data)

# Predict
if st.button("Estimate Price"):
    prediction = model.predict(input_df)
    st.success(f"Estimated Property Price: £{prediction[0]:,.2f}")
