import streamlit as st
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("🏠 Welcome to Quantum Mentor")
st.markdown("""
This platform helps you:
- Understand quantum concepts with clarity
- Simulate quantum-style decisions
- Prepare for science seminars and hackathons

Explore the modules using the sidebar.  
Let’s decode the future—together.
""")
quantum_footer()
