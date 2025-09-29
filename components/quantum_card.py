import streamlit as st
import random
def quantum_riddle():
    riddles = [
        "I am neither 0 nor 1, yet I am both. What am I?",
        "Two particles, far apart, yet one fate. What binds them?",
        "I collapse when you look, but exist when you don’t. Who am I?",
        "I solve problems faster than thought, but only when cold. What am I?"
    ]
    st.markdown(f"🧩 **Riddle of the Day:** *{random.choice(riddles)}*")

def quantum_mentor_avatar():
    quotes = [
        "🌌 *In the dance of particles, truth hides in probability.*",
        "🧩 *What is seen changes what is real—observe wisely.*",
        "🔮 *I am both here and not—until you ask.*",
        "🧠 *A question unasked is a qubit unmeasured.*",
        "🌿 *Even chaos has symmetry—find the pattern beneath.*",
        "⚛️ *What binds two minds across space? Entanglement of curiosity.*",
        "🕰️ *Time bends when thought deepens—dare to think differently.*"
    ]
    st.markdown(f"""
    <div style='border:1px solid #ccc; padding:10px; border-radius:10px; background-color:#f9f9f9'>
        <h4>🧙 Quantum Mentor Says:</h4>
        <em>{random.choice(quotes)}</em>
    </div>
    """, unsafe_allow_html=True)
