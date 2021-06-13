import streamlit as st
import numpy as np
import pandas as pd
import joblib




st.title("STROKE PREDICTION")
df_newdata = pd.DataFrame()

option = st.sidebar.selectbox('What do you want to do?',('Query', 'Donate Data'))
st.write("MODE",option)

gender = st.slider('What\'s your gender?', 0, 1, 0,key='1')
st.write("Male" if gender == 1 else "Female")

age = st.slider('How old are you?', 0, 130, 25,key='2')
st.write("I'm {} old".format(age))

hypertension = st.slider('Do you have a hypertension?', 0, 1, 0,key='3')
st.write("Hyper" if hypertension == 1 else "Lower")

glu = st.number_input('What\'s your average glucose level? (mg/100ml blood)')

bmi = st.number_input('What\'s your BMI?')


if option == 'Query':
    model = joblib.load("model_MLP_SGD_fitted.pkl")
    result = model.predict(pd.DataFrame([[gender,age,hypertension,glu,bmi]]))
    st.write(result)
    st.write("You may have a stoke of highly probability! Be careful!" if result == 1 else "You are absolutely health! Congratulate!")
else:
    submit = st.button("submit")
    state = st.radio("Have you stroked?",['Yes','Never'])
    state_index = [1 if state == 'Yes' else 0]
    if submit:
        st.write("Thanks for donating data! We will retrain our dataset and provide more precise service!")
        st.write("Your personal physical condition:")
        st.write(pd.DataFrame([[gender,age,hypertension,glu,bmi,state_index[0]]]))
