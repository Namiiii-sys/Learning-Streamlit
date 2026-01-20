import streamlit as st


st.title("Hello Streamlit App")
st.subheader("Made by Namita")
st.text("welcome to my first interactive app")
st.write("Choose your favourite Drink")


drink = st.selectbox("Your fav Drink: ", ["Tea","coffee","Juice"])
st.write(f"You choose {drink}. Nice Choice!")

st.success("Your Drink is Ready!")