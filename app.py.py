

import streamlit as st

st.set_page_config(
    page_title="Rj Deguzman Amit | Portfolio",
    page_icon="🌟",
    layout="wide"
)

st.title("Rj Deguzman Amit")
st.subheader("My Personal Portfolio")

page = st.sidebar.radio(
    "Explore My Website",
    ["Home", "About Me", "Education",
     "Hobbies & Interests", "Skills", "My Goals"]
)

if page == "Home":
    st.header("Welcome to My Personal Portfolio")
    st.image("profile.jpg", width=280)
    st.write("""
    Hello and welcome! I am Rj Deguzman Amit.
    I am a second-year Mechanical Engineering student
    who enjoys learning new things and developing new skills.
    """)
    st.info("Explore the pages using the menu on the left.")

elif page == "About Me":
    st.header("About Me")
    st.image(
        "https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=1000"
    )
    st.write("""
    Hello! My name is Rj Deguzman Amit. I am currently
    a second-year Mechanical Engineering student.

    I am a dedicated and goal-oriented individual who
    enjoys learning new things, developing my skills,
    and challenging myself to become a better person.

    My goal is to improve my knowledge, gain more experience,
    learn how to earn money responsibly, and become a
    successful Mechanical Engineer while building my own
    business in the future.
    """)

elif page == "Education":
    st.header("My Education")
    st.image(
        "https://images.unsplash.com/photo-1562774053-701939374585?w=1000"
    )
    st.subheader("NEMSU")
    st.write("Year Level: Second Year College")
    st.write("Course: Bachelor of Science in Mechanical Engineering")

elif page == "Hobbies & Interests":
    st.header("My Hobbies and Interests")

    st.subheader("Gaming")
    st.image("https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1000")

    st.subheader("Playing Sports")
    st.image("https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=1000")

    st.subheader("Reading")
    st.image("https://images.unsplash.com/photo-1512821838-2c9b4c3f6b3c?w=1000")

    st.subheader("Learning New Things and Programming")
    st.image("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1000")

    st.subheader("Listening to Music")
    st.image("https://images.unsplash.com/photo-1511379938547-c1f69419868d?w=1000")

elif page == "Skills":
    st.header("My Skills")
    st.image(
        "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1000"
    )
    st.subheader("Computer Troubleshooting")
    st.write("I enjoy fixing computers and solving computer problems.")
    st.subheader("Programming")
    st.write("I am interested in learning programming and improving my skills.")

elif page == "My Goals":
    st.header("My Goals")
    st.image(
        "https://images.unsplash.com/photo-1581092921461-eab62e97a780?w=1000"
    )
    st.write("""
    My goals are to become a successful Mechanical Engineer
    and build my own business in the future.

    I want to continue learning, gain experience,
    improve my skills, and work hard to achieve my dreams.
    """)

st.sidebar.markdown("---")
st.sidebar.caption("© Rj Deguzman Amit | Personal Portfolio")
