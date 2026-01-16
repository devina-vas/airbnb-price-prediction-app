# 🏠 Airbnb Price Prediction App

This project is an end-to-end **Machine Learning web application** that predicts the price of an Airbnb listing based on key property and host-related features. The application is built using **Python, Scikit-learn, and Streamlit**, and demonstrates the complete workflow from data preprocessing to model deployment.

---

##  Project Objective

The primary objective of this project is to help Airbnb hosts determine an optimal listing price by leveraging historical data and machine learning techniques. Accurate price prediction enables hosts to remain competitive while maximizing revenue.

---

## Machine Learning Approach

- **Problem Type:** Regression  
- **Final Model Used:** Linear Regression  
- **Target Variable:** `log_price` (log-transformed listing price)

Although advanced models like Random Forest and XGBoost were explored, Linear Regression was selected as the final model due to:
- Faster execution time
- Better interpretability
- Computational efficiency on local systems
- Stable baseline performance

---

##  Features Used in the Model

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

These features were selected to ensure consistency between model training and the web application inputs.

---

##  Data Preprocessing

- Missing values handled using **scikit-learn pipelines**
- Numerical features imputed using median and scaled
- Categorical features imputed using mode and one-hot encoded
- Feature engineering performed for amenities count, host experience, and neighbourhood popularity
- Preprocessing and model training combined using a single pipeline to prevent data leakage

---

##  Web Application (Streamlit)

The trained model was deployed as a **Streamlit web application** that:
- Accepts user input through an interactive UI
- Applies the same preprocessing steps used during training
- Predicts the Airbnb listing price in real time
- Displays results in a user-friendly format

---

##  Project Structure

airbnb-price-prediction-app/  


├── app.py # Streamlit application code  

├── airbnb_price_model.pkl # Trained ML pipeline  

├── requirements.txt # Required Python libraries  

├── README.md # Project documentation  



---

## ▶️ How to Run the App Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/airbnb-price-prediction-app.git

2. Navigate to the project directory:
   ```bash
   cd airbnb-price-prediction-app
3. Install dependencies and Run the Streamlit app:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py

## Deployment

The application can be deployed using Streamlit Community Cloud by connecting this GitHub repository. Once deployed, the app is accessible through a public URL.

## Model Evaluation

Model performance was evaluated using:

RMSE (Root Mean Squared Error)

MAE (Mean Absolute Error)

R² Score

An Actual Price vs Predicted Price comparison was also used to validate prediction accuracy.

---

## Key Insights

Listings with more amenities tend to have higher prices

Entire homes are priced higher than private or shared rooms

Neighbourhood popularity significantly impacts pricing

Host experience contributes to better pricing strategies

## Technologies Used

Python

Pandas, NumPy

Scikit-learn

Streamlit

Joblib

GitHub
   
      










