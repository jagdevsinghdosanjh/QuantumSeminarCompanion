import streamlit as st
import pandas as pd
from components.header_footer import quantum_header, quantum_footer
from utils.badge_engine import assign_badges

quantum_header()
st.title("🏅 Quantum Mentor Badge Tracker")

st.markdown("""
Track student progress across core modules:  
- 🧠 Quantum Explorer  
- 📚 Quantum Quiz  
- 🧙 Wisdom Wall  
- 🎮 Challenge Week  
- 🎓 Certificate Generator
""")

# Sidebar: Add student
st.sidebar.header("➕ Add Student Progress")
student_name = st.sidebar.text_input("Student Name")
explorer = st.sidebar.checkbox("Quantum Explorer")
quiz = st.sidebar.checkbox("Quantum Quiz")
wisdom = st.sidebar.checkbox("Wisdom Wall")
challenge = st.sidebar.checkbox("Challenge Week")
certificate = st.sidebar.checkbox("Certificate Generator")

if "student_data" not in st.session_state:
    st.session_state.student_data = []

if st.sidebar.button("Add to Tracker") and student_name:
    st.session_state.student_data.append({
        "Student Name": student_name,
        "Quantum Explorer": explorer,
        "Quantum Quiz": quiz,
        "Wisdom Wall": wisdom,
        "Challenge Week": challenge,
        "Certificate": certificate
    })

# Display tracker table
if st.session_state.student_data:
    df = pd.DataFrame(st.session_state.student_data)

    # Convert boolean to emoji
    emoji_df = df.copy()
    for col in df.columns[1:]:
        emoji_df[col] = df[col].apply(lambda x: "✅" if x else "❌")

    st.dataframe(emoji_df, width='stretch')

    # Badge preview
    st.markdown("### 🏅 Badge Preview")
    for student in st.session_state.student_data:
        completed_modules = sum([student["Quantum Explorer"], student["Quantum Quiz"],
                                 student["Wisdom Wall"], student["Challenge Week"], student["Certificate"]])
        score = 5 if student["Quantum Quiz"] else 3  # Simulated score
        badges = assign_badges(score, completed_modules)
        st.markdown(f"**{student['Student Name']}** → {' • '.join(badges) if badges else 'No badges yet'}")

else:
    st.warning("No student data yet. Use the sidebar to add entries.")

st.markdown("---")
st.info("Educators can export this table to Excel or Google Sheets for real-time tracking and badge assignment.")

quantum_footer()
