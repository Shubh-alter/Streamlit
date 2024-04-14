import streamlit as st
import numpy as np
import pandas as pd


st.title("Hello Everyone")

btn = st.button("Click me")


np.random.seed(0)
dates = pd.date_range('2022-01-01', periods=100)
sales_data = pd.DataFrame({
    'Date': dates,
    'Sales': np.random.randint(100, 1000, size=len(dates))
})

st.checkbox("Male" )
st.checkbox("female" )

if btn:
    st.write("Intro to Streamlit")
    st.camera_input("hello")
    st.bar_chart(data=sales_data.set_index('Date'))