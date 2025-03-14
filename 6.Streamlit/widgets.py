import streamlit as st
import pandas as pd

# Title
st.title("Streamlit Text Input")

# Text Input
name = st.text_input("Enter your name")

age = st.slider("Select your age",0,100,25)

st.write(f"Your age is {age}.")

options = ["Python","Javascript","Java","C++"]
choice = st.selectbox("Choose your favourite language",options)
st.write(f"You selected {choice}")


if name:
    st.write("Hello, " + name + "!")


data = {
    "Name": ["John", 'Jane', 'Jake', 'Jill'],
    "Age": [28,45,46,87],
    "Language": ["Python","Javascript","Java","C++"]
}

df = pd.DataFrame(data)
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file to upload",type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)