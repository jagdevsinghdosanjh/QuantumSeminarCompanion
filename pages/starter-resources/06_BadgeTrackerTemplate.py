import streamlit as st
from components.header_footer import quantum_header, quantum_footer

quantum_header()
st.title("🏅 Badge Tracker Template")

st.markdown("""
Use this template to track student progress across modules:  
- Quantum Explorer  
- Quantum Quiz  
- Wisdom Wall  
- Challenge Week  
- Certificate Generator
""")

st.markdown("""
| Student Name | Explorer | Quiz | Wisdom Wall | Challenge Week | Certificate |
|--------------|----------|------|-------------|----------------|-------------|
| Aditi        | ✅       | ✅   | ✅          | ✅             | ✅          |
| Rohan        | ✅       | ✅   | ❌          | ❌             | ❌          |
| Meera        | ✅       | ✅   | ✅          | ✅             | ✅          |
""")

st.info("Educators can copy this into Excel or Google Sheets and customize it for their classroom.")

quantum_footer()
