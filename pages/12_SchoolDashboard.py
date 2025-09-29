import streamlit as st
import json
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("🏫 Quantum Mentor School Dashboard")
st.markdown("Track student progress across classrooms and generate engagement reports.")

# Load leaderboard data
try:
    with open("data/leaderboard.json", "r") as f:
        leaderboard = json.load(f)
except FileNotFoundError:
    st.warning("Leaderboard file not found. No student data available.")
    leaderboard = []
except json.JSONDecodeError:
    st.error("Leaderboard file is corrupted. Unable to load student data.")
    leaderboard = []

# Display engagement overview
if leaderboard:
    st.subheader("📊 Engagement Overview")
    total_students = len(leaderboard)
    avg_score = sum([entry.get("score", 0) for entry in leaderboard]) / total_students
    st.write(f"Total Students: {total_students}")
    st.write(f"Average Quiz Score: {avg_score:.2f}/5")
    st.markdown("---")

    st.subheader("🎓 Student Progress")
    for entry in leaderboard:
        name = entry.get("name", "Unnamed")
        score = entry.get("score", 0)
        badges = entry.get("badges", [])
        st.markdown(f"**{name}** – Score: {score}/5 – Badges: {', '.join(badges)}")
        st.markdown("---")
else:
    st.info("No student progress data available yet.")
quantum_footer()

# import streamlit as st
# import json

# st.title("🏫 Quantum Mentor School Dashboard")
# st.markdown("Track student progress across classrooms and generate engagement reports.")

# try:
#     with open("data/leaderboard.json", "r") as f:
#         leaderboard = json.load(f)

#     st.subheader("📊 Engagement Overview")
#     st.write(f"Total Students: {len(leaderboard)}")
#     avg_score = sum([entry["score"] for entry in leaderboard]) / len(leaderboard)
#     st.write(f"Average Quiz Score: {avg_score:.2f}/5")

#     st.subheader("🎓 Student Progress")
#     for entry in leaderboard:
#         st.markdown(f"**{entry['name']}** – Score: {entry['score']}/5 – Badges: {', '.join(entry['badges'])}")
#         st.markdown("---")
# except:
#     st.warning("No student data available yet.")
