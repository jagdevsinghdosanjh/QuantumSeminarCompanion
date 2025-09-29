import streamlit as st
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("🧾 Printable Dashboard Summary")
st.markdown("Generate a printable summary of your Quantum Mentor journey.")

if "student_name" in st.session_state:
    name = st.session_state["student_name"]
    st.subheader(f"Student: {name}")
    quiz_score = st.slider("Quiz Score", 0, 5, 4)
    modules = st.multiselect("Modules Completed", [
        "Quantum Quiz", "Wisdom Wall", "Logic Simulator", "Hackathon Helper", "Certificate"
    ])
    final_badge = "Quantum Mentor Champion" if len(modules) == 5 and quiz_score >= 4 else "Quantum Explorer"

    st.markdown("---")
    st.markdown(f"""
    ### Quantum Mentor Summary for {name}
    - Quiz Score: {quiz_score}/5
    - Modules Completed: {', '.join(modules)}
    - Final Badge: 🧙 {final_badge}
    - Date: {st.date_input("Date", value=None)}
    """)
    st.info("You can print this page using your browser's print option (Ctrl+P).")
else:
    st.warning("Please log in using the sidebar to generate your summary.")
quantum_footer()