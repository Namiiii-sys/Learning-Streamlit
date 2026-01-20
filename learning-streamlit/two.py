import streamlit as st

#Widgets

st.title("Drink Maker app")

if st.button("Make Drink"):
    st.success("Your drink is being made ready")

ice = st.checkbox("Add Ice")

if ice:
    st.write("Ice Added!")

drink_type = st.radio("Pick your drink base: ",["sugar","Milk","Almond milk","Lemon","Orange"])
st.write(f"Selected the base of {drink_type} successfully")

flavour = st.selectbox("Choose flavour: ",["Masala","Hazelnut","Americano","Orange","Lemon"])

sugar = st.slider("Sugar level (Spoon)", 0, 5, 2)

cups = st.number_input("How many Cups", min_value=1 , max_value=50, step=1)
st.write(f"Selected {cups} cups.")


name = st.text_input("Enter your name")
if name:
    st.write(f"Welcome, {name}! Your Drink is on the way!")


dob = st.date_input("Select your date of birth")
st.write(f"Your date of birth is: {dob}")
