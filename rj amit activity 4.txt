
import streamlit as st

# My Full Name
st.header("RJ D. AMIT")

# Application Title
st.title("My First Streamlit Web Application")

# Introduction
st.write("Welcome to my Streamlit application!")

# Text Input
name = st.text_input("Enter your name:")

if name:
    st.write("Hello,", name)

# Button
if st.button("Click Me"):
    st.success("My application is working!")

# Slider
age = st.slider("Select your age:", 1, 100, 18)

st.write("Your selected age is:", age)
