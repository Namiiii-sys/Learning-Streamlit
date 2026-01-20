import streamlit as st
from datetime import date

st.title("Age Calculator")
st.subheader("An app which automatically calculates your age for you")

today = date.today()

dob = st.date_input("Select your date of birth" , min_value=date(1900,1,1),max_value=today)

if dob:
    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age-=1

    st.success(f"You are {age} years old!")