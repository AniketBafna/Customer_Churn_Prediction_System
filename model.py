import streamlit as st
import pickle
import numpy as np
import pandas as pd


pipe = pickle.load(open('pipe.pkl', 'rb'))

df = pd.read_csv('telecom_data_clean.csv')

#st.dataframe(df)

def model():
    st.header("Telecom Customer Churn Predictor")

    gender = df['gender'].sort_values().unique()
    senior = df['SeniorCitizen'].sort_values().unique()
    multilines = df['MultipleLines'].sort_values().unique()
    internet = df['InternetService'].sort_values().unique()
    security = df['OnlineSecurity'].sort_values().unique()
    backup = df['OnlineBackup'].sort_values().unique()
    protection = df['DeviceProtection'].sort_values().unique()
    support = df['TechSupport'].sort_values().unique()
    tv = df['StreamingTV'].sort_values().unique()
    movies = df['StreamingMovies'].sort_values().unique()
    contract = df['Contract'].sort_values().unique()
    billing = df['PaperlessBilling'].sort_values().unique()
    paymentmethod = df['PaymentMethod'].sort_values().unique()


    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender",gender)
    with col2:
        senior = st.selectbox("Senior Citizen",senior)

    col3, col4 = st.columns(2)
    with col3:
        multilines = st.selectbox("Multiple Lines",multilines)
    with col4:
        internet = st.selectbox('Internet Service',internet)

    col5, col6, col7 = st.columns(3)
    with col5:
        security = st.selectbox('Online Security', security)
    with col6:
        backup = st.selectbox('Online Backup', backup)
    with col7:
        protection = st.selectbox('Device Protection', protection)

    col8, col9, col10 = st.columns(3)
    with col8:
        support = st.selectbox('Tech Support', support)
    with col9:
        tv = st.selectbox('Streaming TV', tv)
    with col10:
        movies = st.selectbox('StreamingMovies', movies)

    col11, col12, col13 = st.columns(3)
    with col11:
        contract = st.selectbox('Contract', contract)
    with col12:
        billing = st.selectbox('Paperless Billing', billing)
    with col13:
        paymentmethod = st.selectbox('Payment Method', paymentmethod)

    col14, col15, col16 = st.columns(3)
    with col14:
        tenure = st.number_input("Tenure (in Months)")
    with col15:
        monthly = st.number_input("Monthly Charges")
    with col16:
        yearly = st.number_input("Yearly Charges")

    if st.button('Predict Churn'):
        input_df = pd.DataFrame({'gender' :[gender] , 'SeniorCitizen' :[senior], 'tenure':[tenure], 'MultipleLines':[multilines], 
                             'InternetService':[internet], 'OnlineSecurity':[security], 'OnlineBackup':[backup], 
                             'DeviceProtection':[protection], 'TechSupport':[support], 'StreamingTV':[tv], 
                             'StreamingMovies':[movies], 'Contract':[contract], 'PaperlessBilling':[billing],
                             'PaymentMethod':[paymentmethod], 'MonthlyCharges':[monthly], 'TotalCharges':[yearly]})
        result = pipe.predict(input_df)
        if result == "Yes":
            st.header("The Customer will Churn")
        else:
            st.header("The Customer will not Churn")