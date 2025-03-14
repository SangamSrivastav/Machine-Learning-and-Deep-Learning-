import streamlit as st
import numpy as np
import pandas as pd

## Title of the application
st.title("Hello Streamlit")

## Display simple text
st.write("This is a simple text.")

## Create a simple dataframe

df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column' : [5,6,7,8]
})

## Display the dataframe

st.write("This is a simple dataframe")
st.dataframe(df)

## Create a simple chart

chart_data = pd.DataFrame(
    np.random.randn(20, 3),columns=['a','b','c']
)
st.line_chart(chart_data)