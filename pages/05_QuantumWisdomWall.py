import streamlit as st
import json
from datetime import datetime
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("🧙 Quantum Wisdom Wall")
st.markdown("""
Welcome to the Quantum Wisdom Wall—a space to share your poetic metaphors, scientific riddles, and quantum reflections.  
Let your imagination collapse into clarity.
""")

# Input form
with st.form("wisdom_form"):
    name = st.text_input("Your Name")
    submission = st.text_area("Your Quantum Thought (riddle, metaphor, or reflection)")
    submitted = st.form_submit_button("Submit")

if submitted and name and submission:
    new_entry = {
        "name": name,
        "text": submission,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open("data/wisdom_wall.json", "r") as f:
            wall = json.load(f)
    except FileNotFoundError:
        st.warning("Wisdom wall file not found. Creating a new one.")
        wall = []
    except json.JSONDecodeError:
        st.error("Wisdom wall file is corrupted. Starting fresh.")
        wall = []

    wall.append(new_entry)

    try:
        with open("data/wisdom_wall.json", "w") as f:
            json.dump(wall, f, indent=2)
        st.success("🧠 Your wisdom has been added to the wall!")
    except IOError:
        st.error("Failed to save your submission. Please try again later.")

# Display entries
st.markdown("---")
st.subheader("🧩 Student Submissions")

try:
    with open("data/wisdom_wall.json", "r") as f:
        wall = json.load(f)
    if wall:
        for entry in reversed(wall[-10:]):  # Show last 10 entries
            st.markdown(f"**{entry['name']}** wrote at *{entry['timestamp']}*:")
            st.markdown(f"> {entry['text']}")
            st.markdown("---")
    else:
        st.info("No submissions yet. Be the first to add your quantum wisdom!")
except FileNotFoundError:
    st.info("Wisdom wall file not found. Be the first to add your quantum wisdom!")
except json.JSONDecodeError:
    st.warning("Wisdom wall file is corrupted. No entries to display.")

quantum_footer()

# import streamlit as st
# import json
# from datetime import datetime

# st.title("🧙 Quantum Wisdom Wall")
# st.markdown("""
# Welcome to the Quantum Wisdom Wall—a space to share your poetic metaphors, scientific riddles, and quantum reflections.  
# Let your imagination collapse into clarity.
# """)

# # Input form
# with st.form("wisdom_form"):
#     name = st.text_input("Your Name")
#     submission = st.text_area("Your Quantum Thought (riddle, metaphor, or reflection)")
#     submitted = st.form_submit_button("Submit")

# if submitted and name and submission:
#     new_entry = {
#         "name": name,
#         "text": submission,
#         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     }
#     try:
#         with open("data/wisdom_wall.json", "r") as f:
#             wall = json.load(f)
#     except:
#         wall = []

#     wall.append(new_entry)
#     with open("data/wisdom_wall.json", "w") as f:
#         json.dump(wall, f, indent=2)

#     st.success("🧠 Your wisdom has been added to the wall!")

# # Display entries
# st.markdown("---")
# st.subheader("🧩 Student Submissions")
# try:
#     with open("data/wisdom_wall.json", "r") as f:
#         wall = json.load(f)
#     for entry in reversed(wall[-10:]):  # Show last 10 entries
#         st.markdown(f"**{entry['name']}** wrote at *{entry['timestamp']}*:")
#         st.markdown(f"> {entry['text']}")
#         st.markdown("---")
# except:
#     st.info("No submissions yet. Be the first to add your quantum wisdom!")
