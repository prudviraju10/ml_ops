import streamlit as st
import pickle
import pandas as pd
import numpy as np
import datetime


st.write("Chance of Admit")

df = pd.read_csv(
    "https://d2beiqkhq929f0.cloudfront.net/public_assets/assets/000/001/839/original/Jamboree_Admission.csv")

st.dataframe(df[:20])
# model = pickle.load(open("model.pkl", "rb"))
model = pickle.load(open("lr.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.divider()

gre_score = st.slider('what is your gre score?', 0, 360, 250)
st.write("my gre score is ", gre_score)

st.divider()

toefl_score = st.slider('what is your toefl score?', 0, 120, 100)
st.write("my toefl score is ", toefl_score)

st.divider()

univ_rating = st.slider('what is your university rating?', 1, 5, 1)
st.write("my university rating is ", univ_rating)

st.divider()

sop = st.slider('what is your sop?', 1, 5, 1)
st.write("my sop is ", sop)

st.divider()

lor = st.slider('what is your lor?', 1, 5, 1)
st.write("my lor is ", lor)

st.divider()

cgpa = st.number_input('what is your cgpa?', min_value=0.0,
                       max_value=10.0, placeholder="a value between 0 to 10", step=0.1)
st.write('my cgpa is ', cgpa)

st.divider()

reaserch = st.radio("Have you done research?", ["Yes", "No"],)


reaserch_val = 0

if reaserch == 'Yes':
    st.write('You selected Yes.')
    reaserch_val = 1
else:
    st.write("You selected No.")

st.divider()

if st.button('Predict'):
    # val = model.predict([[-0.362110, -1.488239, -1.802983, 0.140430, -0.523883, -0.640246, 0.899975]])
    val = model.predict(scaler.transform(
        [[gre_score, toefl_score, univ_rating, sop, lor, cgpa, reaserch_val]]))
    st.write(val)
else:
    st.write('Know your chnace of admit')
