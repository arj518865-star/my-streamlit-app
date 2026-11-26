import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Rj Deguzman Amit | Personal Portfolio",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

.stApp {
    background: linear-gradient(145deg, #f7f9fc 0%, #eef3fa 55%, #f8fafc 100%);
    color: #172033;
    font-family: 'DM Sans', sans-serif;
}
.block-container {max-width: 1120px; padding-top: 2.4rem; padding-bottom: 3rem;}
h1, h2, h3 {font-family: 'Manrope', sans-serif; color: #14213d;}
.hero {
    background: linear-gradient(120deg, #14213d 0%, #1d3557 60%, #315b83 100%);
    border-radius: 28px;
    padding: 2.5rem;
    color: white;
    box-shadow: 0 18px 45px rgba(20, 33, 61, .16);
    margin-bottom: 1.5rem;
}
.hero h1 {color: white; font-size: clamp(2rem, 5vw, 3.35rem); margin: .25rem 0 .6rem 0;}
.hero p {color: #e5edf7; font-size: 1.05rem; line-height: 1.7;}
.eyebrow {text-transform: uppercase; letter-spacing: .18em; color: #a9c7e8; font-size: .76rem; font-weight: 700;}
.pill {
    display: inline-block; background: rgba(255,255,255,.13); color: #f3f7fc;
    border: 1px solid rgba(255,255,255,.22); border-radius: 999px;
    padding: .45rem .8rem; margin: .25rem .25rem .1rem 0; font-size: .82rem;
}
.section-card {
    background: white; border: 1px solid #e5eaf1; border-radius: 20px;
    padding: 1.35rem 1.5rem; height: 100%;
    box-shadow: 0 8px 24px rgba(31, 51, 79, .045);
}
.section-card h3 {margin-top: 0; font-size: 1.12rem;}
.muted {color: #64748b; line-height: 1.75;}
.tag {
    display: inline-block; background: #edf4fb; color: #23466c;
    border-radius: 999px; padding: .42rem .75rem; margin: .22rem .18rem;
    font-size: .88rem; font-weight: 600;
}
.footer {text-align:center; color:#718096; font-size:.85rem; padding-top:2rem;}
div[data-testid="stImage"] img {border-radius: 22px; object-fit: cover;}
</style>
""", unsafe_allow_html=True)

# ---------- Hero ----------
left, right = st.columns([1, 2.15], gap="large", vertical_alignment="center")
with left:
    image_file = Path(__file__).parent / "profile.jpg"
    if image_file.exists():
        st.image(str(image_file), use_container_width=True)
    else:
        st.info("Add your photo as profile.jpg in the same folder as app.py.")
with right:
    st.markdown("""
    <div class="hero">
      <div class="eyebrow">Personal Portfolio</div>
      <h1>Hi, I'm Rj Deguzman Amit</h1>
      <p>Mechanical Engineering student, curious learner, and future entrepreneur.
      I enjoy exploring technology, developing practical skills, and taking on new challenges.</p>
      <span class="pill">Mechanical Engineering</span>
      <span class="pill">Programming Learner</span>
      <span class="pill">Future Entrepreneur</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## About Me")
st.markdown("""
<div class="section-card">
<p class="muted">
Hello! My name is <strong>Rj Deguzman Amit</strong>. I am a second-year
Bachelor of Science in Mechanical Engineering student at NEMSU.
I am a dedicated and goal-oriented individual who enjoys learning new things,
developing my skills, and challenging myself to grow.
</p>
<p class="muted">
I am especially interested in learning programming and discovering how technology
can solve practical problems. I hope to gain experience, become a successful
mechanical engineer, and build my own business in the future.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("")
st.markdown("## My Profile")
c1, c2, c3 = st.columns(3, gap="medium")
with c1:
    st.markdown("""
    <div class="section-card">
      <h3>🎓 Education</h3>
      <p><strong>North Eastern Mindanao State University (NEMSU)</strong></p>
      <p class="muted">Second Year College<br>Bachelor of Science in Mechanical Engineering</p>
    </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="section-card">
      <h3>🛠️ Skills</h3>
      <p class="muted">• Computer troubleshooting<br>• Fixing computer issues<br>• Eager to learn programming</p>
    </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown("""
    <div class="section-card">
      <h3>🚀 Future Goals</h3>
      <p class="muted">• Become a successful mechanical engineer<br>• Gain knowledge and experience<br>• Build my own business</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("")
st.markdown("## Hobbies & Interests")
st.markdown("""
<span class="tag">🎮 Gaming</span>
<span class="tag">🏀 Playing Sports</span>
<span class="tag">📚 Reading</span>
<span class="tag">💻 Learning Programming</span>
<span class="tag">🎵 Listening to Music</span>
<span class="tag">🌱 Learning New Things</span>
""", unsafe_allow_html=True)

st.markdown("")
st.markdown("## A Little More About Me")
st.markdown("""
<div class="section-card">
<p class="muted">
I believe that consistent learning and determination can open opportunities.
Whether I am learning something new, solving a computer problem, or working
toward my studies, I aim to keep improving one step at a time.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="footer">Thank you for visiting my personal portfolio.</div>', unsafe_allow_html=True)
