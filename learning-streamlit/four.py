import streamlit as st
import pandas as pd


st.title("Drink Insight Dashboard")

file = st.file_uploader("upload your csv file",type=['csv'])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary Stats")
    st.write(df.describe())

if file:
    drinks= df["drink_name"].unique()
    selected_drink = st.selectbox("Filter by drinks", drinks)
    filtered_data=df[df["drink_name"] == selected_drink]
    st.dataframe(filtered_data)