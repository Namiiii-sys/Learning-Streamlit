import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("CSV Insights Dashboard")

file = st.file_uploader("Upload a Csv file", ["csv"])
if file:
    df = pd.read_csv(file)


    col1 , col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing values", df.isna().sum().sum())

    st.divider()
    
    st.subheader("Data Preview")
    st.dataframe(df.head())

    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    
    if len(numeric_cols) > 0:
        selected_col = st.selectbox("Select a numeric column to visualize",numeric_cols)
   
        st.subheader("Summary Statistics")
        st.write({
            "Mean" : round(df[selected_col].mean(), 2),
            "Min" : int(df[selected_col].min()),
            "Max" : int(df[selected_col].max())
        })

        st.subheader(f"Visualisations of {selected_col}")
        
        col3,col4 = st.columns(2)
        with col3:
            st.write(f"Distribution of {selected_col}")
            st.bar_chart(df[selected_col])

        with col4:
            st.write(f"Value Change across rows of {selected_col}")
            st.line_chart(df[selected_col])

        with st.expander("Raw data"):
            st.dataframe(df)

            csv = df.to_csv(index=False)
            st.download_button(
                label="Download Raw Data",
                data=csv,
                file_name="raw_Data.csv",
                mime = "text/csv"
            )
    else:
        st.warning("No Numeric Dataset found.")
else:
    st.info("Please upload a csv file to get started")