import streamlit as st
import pickle
import pandas as pd
import numpy as np
import datetime

st.write("Hello World")
df = pd.read_csv(
    "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/003/549/original/logistic_regression.csv?1651045921")

st.dataframe(df[:20])
model = pickle.load(open("model.pkl", "rb"))

col1, col2, col3 = st.columns(3)

with col1:
    val1 = st.selectbox("select a number", (1, 2, 3, 4), index=None)
    st.write("you have selected", val1)

with col2:
    val2 = st.radio("select a number", (1, 2, 3, 4))
    st.write("you have selected", val2)

with col3:
    val3 = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", val3, 'years old')

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)


if st.button("Run algo", type="primary"):
    st.write("model will run")
