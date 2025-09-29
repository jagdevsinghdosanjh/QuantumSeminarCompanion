import streamlit as st
import json
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("🧑‍🏫 Contributor Dashboard")
st.markdown("Track student engagement and module completion.")

# Load Wisdom Wall entries
try:
    with open("data/wisdom_wall.json", "r") as f:
        wisdom_entries = json.load(f)
except FileNotFoundError:
    st.warning("Wisdom Wall file not found. No submissions to display.")
    wisdom_entries = []
except json.JSONDecodeError:
    st.error("Wisdom Wall file is corrupted. Unable to load submissions.")
    wisdom_entries = []

# Load Leaderboard entries
try:
    with open("data/leaderboard.json", "r") as f:
        leaderboard = json.load(f)
except FileNotFoundError:
    st.warning("Leaderboard file not found. No quiz data available.")
    leaderboard = []
except json.JSONDecodeError:
    st.error("Leaderboard file is corrupted. Unable to load quiz data.")
    leaderboard = []

# Display Wisdom Wall summary
st.subheader("📚 Wisdom Wall Contributions")
st.write(f"Total submissions: {len(wisdom_entries)}")
st.markdown("---")

# Display Leaderboard summary
st.subheader("🎯 Quiz Performance Summary")
if leaderboard:
    for entry in leaderboard:
        name = entry.get("name", "Unnamed")
        score = entry.get("score", 0)
        badges = entry.get("badges", [])
        st.write(f"{name} – Score: {score}/5 – Badges: {', '.join(badges)}")
else:
    st.info("No quiz submissions available yet.")

quantum_footer()

# import streamlit as st
# import json

# st.title("🧑‍🏫 Contributor Dashboard")
# st.markdown("Track student engagement and module completion.")

# try:
#     with open("data/wisdom_wall.json", "r") as f:
#         wisdom_entries = json.load(f)
#     with open("data/leaderboard.json", "r") as f:
#         leaderboard = json.load(f)

#     st.subheader("📚 Wisdom Wall Contributions")
#     st.write(f"Total submissions: {len(wisdom_entries)}")
#     st.markdown("---")

#     st.subheader("🎯 Quiz Performance Summary")
#     for entry in leaderboard:
#         st.write(f"{entry['name']} – Score: {entry['score']}/5 – Badges: {', '.join(entry['badges'])}")
# except:
#     st.warning("No data available yet.")
