import streamlit as st
from components.sidebar import render_sidebar
from components.login import student_login
from components.header_footer import quantum_header, quantum_footer
quantum_header()

st.set_page_config(page_title="Quantum Mentor", layout="wide")

st.subheader("📦 Starter- Video Resources")
st.markdown("""
- [Quantum Age Begins - Potentials and Challanges](https://youtu.be/lBlfrN_nCmQ) 
- [For Students By a Student](https://youtu.be/GVcHMowQ7BM)
- [Your thoughts create Reality](https://youtu.be/19-QUNqsGJQ)  
- [How Actully Reflection works at Quantum Level](https://youtu.be/0u7m7YjnfJw)  
- [5 Facts about Quantum Thought](https://youtu.be/DUA0VqfSsf8)
""")

# Sidebar
render_sidebar()
student_login()

# Main content
st.title("🧠 Quantum Mentor")
st.subheader("Explore quantum logic, optimize your ideas, and prepare for the future.")

st.markdown("""
Welcome to **Quantum Mentor**—your interactive companion for science seminars, hackathons, and quantum curiosity.  
Use the sidebar to navigate through modules like:
- 🧪 Quantum Logic Simulator
- 📚 Quantum Glossary & Quiz
- 🚀 Hackathon Helper
""")

# Your page content here...

quantum_footer()


