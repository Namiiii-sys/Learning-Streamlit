import streamlit as st

st.title("Programming language Poll")

col1, col2 , col3= st.columns(3)

with col1:
    st.header("C++")
    vote1 = st.button("Vote C++")
    st.image("https://i.pinimg.com/1200x/c1/63/07/c16307103e86c604c6bc98c78aa84d4b.jpg", width=200)


    
with col2:
    st.header("Java")
    vote2 = st.button("Vote Java")
    st.image("https://i.pinimg.com/736x/87/6b/bb/876bbbdc83de2979d1463cde17d6b6d1.jpg", width=200)

with col3:
    st.header("Python")
    vote3 = st.button("Vote Python")
    st.image("https://i.pinimg.com/1200x/75/65/67/756567d04ec12dac8b72f1582a8ade77.jpg", width=200)


if vote1:
    st.success("Thanks for Voting C++!")

elif vote2:
    st.success("Thanks for Voting Java!")

else:
    st.success("Thanks for Voting Python!")
    
name = st.sidebar.text_input("Enter your name")
tea = st.sidebar.selectbox("choose your language",["cpp","java","python"])

st.write(f'Welcome {name}! ')


with st.expander("Show Instructions for taking cp!"):
    st.write("""
    1. Open the Interface.
    2. Choose the problem.
    3. Write the solution and run test cases.
    4. Submit the solution.
""")
    
st.markdown('### Welcome to our app!')
st.markdown('> Blockcode')