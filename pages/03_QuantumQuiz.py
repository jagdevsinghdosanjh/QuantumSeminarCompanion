import streamlit as st
import json
from random import shuffle
from components.header_footer import quantum_header, quantum_footer

quantum_header()

# Load questions
with open("data/quantum_questions.json", "r") as f:
    questions = json.load(f)

st.title("📚 Quantum Quiz")
st.markdown("Test your understanding of quantum concepts. Select the best answer for each question.")

score = 0
shuffle(questions)

for i, q in enumerate(questions[:5]):
    st.subheader(f"Q{i+1}: {q['question']}")
    selected = st.radio("Choose one:", q["options"], key=i)
    if st.button(f"Submit Q{i+1}", key=f"btn{i}"):
        correct = q["options"][q["answer"][0]]
        if selected == correct:
            st.success("✅ Correct!")
            score += 1
        else:
            st.error(f"❌ Incorrect. Correct answer: {correct}")
        st.info(f"🧠 Explanation: {q['explanation']}")

st.markdown("---")
st.write(f"🎯 Final Score: {score}/5")

quantum_footer()

