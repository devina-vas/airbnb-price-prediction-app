import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page config
st.set_page_config(
    page_title="Airbnb Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Load model
model = joblib.load("airbnb_price_model.pkl")

# Custom CSS
st.markdown("""
<style>
body {
    background-color: #f4f6f9;
}
.main-title {
    text-align: center;
    color: #2c3e50;
}
.subtitle {
    text-align: center;
    color: #7f8c8d;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# Titles
st.markdown("<h1 class='main-title'>🏠 Airbnb Price Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Predict optimal Airbnb listing prices using Machine Learning</p>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

# Inputs
room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])
property_type = st.selectbox("Property Type", ["Apartment", "House", "Condominium"])

col1, col2 = st.columns(2)
with col1:
    accommodates = st.number_input("Accommodates", 1, 16, 2)
    bathrooms = st.number_input("Bathrooms", 1, 10, 1)
    bedrooms = st.number_input("Bedrooms", 0, 10, 1)

with col2:
    beds = st.number_input("Beds", 1, 10, 1)
    amenities_count = st.slider("Amenities Count", 1, 50, 10)
    host_experience_years = st.slider("Host Experience (Years)", 0, 20, 2)

neighbourhood_popularity = st.slider("Neighbourhood Popularity Score", 0, 100, 30)

st.markdown("</div>", unsafe_allow_html=True)

# Prediction
if st.button("🔮 Predict Price"):
    input_df = pd.DataFrame({
        'room_type': [room_type],
        'property_type': [property_type],
        'accommodates': [accommodates],
        'bathrooms': [bathrooms],
        'bedrooms': [bedrooms],
        'beds': [beds],
        'amenities_count': [amenities_count],
        'host_experience_years': [host_experience_years],
        'neighbourhood_popularity': [neighbourhood_popularity]
    })

    log_price = model.predict(input_df)[0]
    price = np.exp(log_price)

    st.success(f"💰 Estimated Airbnb Price: ₹ {price:,.2f}")
    st.info("💡 Tip: Improving amenities and location popularity can increase price.")
