
# 🏠 Airbnb Price Prediction App

This project is an end-to-end **Machine Learning web application** that predicts the price of an Airbnb listing based on key property and host-related features. The application is built using **Python, Scikit-learn, and Streamlit**, and demonstrates the complete workflow from data preprocessing to model deployment.

---

## 📌 Project Objective

The primary objective of this project is to help Airbnb hosts determine an optimal listing price by leveraging historical data and machine learning techniques. Accurate price prediction enables hosts to remain competitive while maximizing revenue.

---

## 🧠 Machine Learning Approach

- **Problem Type:** Regression  
- **Final Model Used:** Linear Regression  
- **Target Variable:** `log_price` (log-transformed listing price)

Although advanced models like Random Forest and XGBoost were explored, Linear Regression was selected as the final model due to:
- Faster execution time
- Better interpretability
- Computational efficiency on local systems
- Stable baseline performance

---

## ⚙️ Features Used in the Model

The deployment-ready model was trained using the following features:

- Room Type  
- Property Type  
- Accommodates  
- Bathrooms  
- Bedrooms  
- Beds  
- Amenities Count  
- Host Experience (Years)  
- Neighbourhood Popularity Score  

These features were selected to ensur
