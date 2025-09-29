import streamlit as st
import json
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("🏆 Quantum Mentor Leaderboard")
st.markdown("Celebrate top performers and badge earners across all modules.")

try:
    with open("data/leaderboard.json", "r") as f:
        leaderboard = json.load(f)
except FileNotFoundError:
    st.warning("Leaderboard file not found. No entries to display yet.")
    leaderboard = []
except json.JSONDecodeError:
    st.error("Leaderboard file is corrupted or improperly formatted.")
    leaderboard = []

if leaderboard:
    for entry in sorted(leaderboard, key=lambda x: x.get("score", 0), reverse=True):
        name = entry.get("name", "Unnamed")
        score = entry.get("score", 0)
        badges = entry.get("badges", [])
        st.markdown(f"### {name} – Score: {score}/5")
        st.markdown("Badges: " + ", ".join(badges))
        st.markdown("---")
else:
    st.info("Leaderboard is empty. Submit your certificate to be featured!")


# Your page content here...

quantum_footer()

# import streamlit as st
# import json

# st.title("🏆 Quantum Mentor Leaderboard")
# st.markdown("Celebrate top performers and badge earners across all modules.")

# try:
#     with open("data/leaderboard.json", "r") as f:
#         leaderboard = json.load(f)

#     for entry in sorted(leaderboard, key=lambda x: x["score"], reverse=True):
#         st.markdown(f"### {entry['name']} – Score: {entry['score']}/5")
#         st.markdown("Badges: " + ", ".join(entry["badges"]))
#         st.markdown("---")
# except:
#     st.info("Leaderboard is empty. Submit your certificate to be featured!")
