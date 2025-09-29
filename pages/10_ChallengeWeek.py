import streamlit as st
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("📅 Quantum Mentor Challenge Week")
st.markdown("""
Welcome to **Challenge Week**!  
Complete all modules between **Oct 1–7** to earn your Quantum Mentor Champion badge.

### How to Participate:
1. Log in with your name
2. Complete the Quantum Quiz (score ≥ 4)
3. Submit to the Wisdom Wall
4. Use the Logic Simulator
5. Visit the Hackathon Helper
6. Generate your certificate

### Rewards:
- 🧙 Quantum Mentor Champion Badge
- 🎓 Printable Certificate
- 🏆 Featured on the Leaderboard
""")

if "student_name" in st.session_state:
    st.success(f"You're logged in as {st.session_state['student_name']}. Start exploring!")
else:
    st.warning("Please log in using the sidebar to begin.")

quantum_footer()