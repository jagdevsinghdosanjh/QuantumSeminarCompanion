import streamlit as st
from utils.challenge_tracker import check_challenge_completion
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("🎮 Quantum Mentor Challenge")
st.markdown("Complete all modules to unlock the final badge and download your dashboard summary.")

# Simulated user data (replace with session-based tracking later)
user_data = {
    "quiz_score": st.slider("Quiz Score", 0, 5, 4),
    "wisdom_submitted": st.checkbox("Submitted to Wisdom Wall"),
    "used_simulator": st.checkbox("Used Logic Simulator"),
    "visited_helper": st.checkbox("Visited Hackathon Helper"),
    "certificate_generated": st.checkbox("Generated Certificate")
}

completed = check_challenge_completion(user_data)

st.markdown(f"✅ Modules Completed: {len(completed)}/5")
for module in completed:
    st.markdown(f"- {module}")

if len(completed) == 5:
    st.success("🎉 Challenge Complete! You've unlocked the Quantum Mentor Badge.")
    st.markdown("🧾 **Dashboard Summary**")
    st.markdown(f"""
    - Name: [Student Name]
    - Quiz Score: {user_data['quiz_score']}/5
    - Modules Completed: {', '.join(completed)}
    - Final Badge: 🧙 Quantum Mentor Champion
    """)
else:
    st.info("Complete all modules to unlock your final badge.")

quantum_footer()
