import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('credit_risk_model.pkl')

st.title("💳 Credit Risk Prediction App")

st.markdown("""
This app predicts whether a loan applicant is a **Good** or **Bad** credit risk based on their profile.
""")

age = st.number_input("Age", min_value=18, max_value=100)
sex = st.selectbox("Sex", ["Male", "Female"])  # 0 = Female, 1 = Male
job = st.selectbox("Job Type", ["Unskilled, non-resident", "Unskilled, resident", "Skilled", "Highly skilled"])  # 0-3
housing = st.selectbox("Housing", ["Own", "Rent", "Free"])  # 0-2
saving_account = st.selectbox("Saving Account", ["Little", "Moderate", "Quite Rich", "Rich", "Unknown"])  # 0-4
checking_account = st.selectbox("Checking Account", ["None", "Little", "Moderate", "Rich"])  # 0-3
credit_amount = st.number_input("Credit Amount (DM)", min_value=0)
duration = st.number_input("Duration (months)", min_value=1)
purpose = st.selectbox("Purpose", ["Car", "Furniture/Equipment", "Radio/TV", "Domestic Appliances", 
                                   "Repairs", "Education", "Business", "Vacation/Others"])  # 0-7


sex_map = {"Male": 1, "Female": 0}
job_map = {
    "Unskilled, non-resident": 0,
    "Unskilled, resident": 1,
    "Skilled": 2,
    "Highly skilled": 3
}
housing_map = {"Own": 1, "Rent": 0, "Free": 2}
saving_map = {"Little": 1, "Moderate": 3, "Quite Rich": 4, "Rich": 2, "Unknown": 0}
checking_map = {"None": 0, "Little": 1, "Moderate": 2, "Rich": 3}
purpose_map = {
    "Car": 0, "Furniture/Equipment": 1, "Radio/TV": 5, "Domestic Appliances": 4,
    "Repairs": 6, "Education": 2, "Business": 3, "Vacation/Others": 7
}


input_data = pd.DataFrame([[
    age,
    sex_map[sex],
    job_map[job],
    housing_map[housing],
    saving_map[saving_account],
    checking_map[checking_account],
    credit_amount,
    duration,
    purpose_map[purpose]
]], columns=['Age', 'Sex', 'Job', 'Housing', 'Saving accounts', 'Checking account', 
             'Credit amount', 'Duration', 'Purpose'])



if st.button("Predict Credit Risk"):
    prediction = model.predict(input_data)
    st.success(f"The applicant is predicted to be: {'Good Credit Risk' if prediction == 1 else 'Bad Credit Risk'}")
