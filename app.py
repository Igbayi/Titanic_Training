import streamlit as st
import pickle


st.title("Salary prediction web Application")

st.write("This web application will help to predict your salary based on your Gender and the year of experience you have worked")


model = pickle.load(open("final model.pkl",'rb'))

Yearofexperience = st.number_input("input you year of experience")
Gender = st.number_input("input your Gender, Male -1 Female - 0")

if st.button('Predict'):
    Pred  = model.predict([[Yearofexperience],[Gender]])
    st.text(f'Your salry is {Pred[0]}')

    st.text("Thank you for using the application")
