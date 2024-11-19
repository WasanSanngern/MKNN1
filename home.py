import streamlit as st
import pandas as pd

st.title("Website Developing using Python")
st.header("Website Developing using Python")

st.subheader("Wasan Sanngern")

st.image('./img/IMG_0689.jpg')
st.subheader("Wasan Sanngern")

dt=pd.read_csv('./data/iris-3.csv')
st.header()
st.write(dt.head(10))