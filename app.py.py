
import streamlit as st

st.set_page_config(page_title="Rj Amit Portfolio", page_icon="🌟", layout="wide")

st.title("Rj Deguzman Amit")
st.subheader("My Personal Portfolio")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "About Me", "Education", "Hobbies", "Skills", "My Goals"]
)

if page == "Home":
    st.header("Welcome to My Portfolio")
    st.image("profile.jpg", width=250)
    st.write("Welcome to my personal website!")

elif page == "About Me":
    st.header("About Me")
    st.image("https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=1000")
    st.write("I enjoy learning new things and exploring technology.")

elif page == "Education":
    st.header("My Education")
    st.image("https://images.unsplash.com/photo-1562774053-701939374585?w=1000")
    st.write("NEMSU")
    st.write("Second Year College")
    st.write("Bachelor of Science in Mechanical Engineering")

elif page == "Hobbies":
    st.header("My Hobbies and Interests")

    st.subheader("Gaming")
    st.image("https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1000")

    st.subheader("Sports")
    st.image("https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=1000")

    st.subheader("Reading")
    st.image("https://images.unsplash.com/photo-1512821838-2c9b4c3f6b3c?w=1000")

    st.subheader("Music")
    st.image("https://images.unsplash.com/photo-1511379938547-c1f69419868d?w=1000")

elif page == "Skills":
    st.header("My Skills")
    st.image("https://images.unsplash.com/photo-1518770660439-4636190af475?w=1000")
    st.write("Computer troubleshooting")
    st.write("Fixing computers")
    st.write("Learning programming")

elif page == "My Goals":
    st.header("My Goals")
    st.image("https://images.unsplash.com/photo-1581092921461-eab62e97a780?w=1000")
    st.write("Become a successful mechanical engineer.")
    st.write("Build my own business.")

st.sidebar.success("Personal Portfolio")
