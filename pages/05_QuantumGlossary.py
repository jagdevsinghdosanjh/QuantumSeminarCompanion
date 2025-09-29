import streamlit as st
from components.header_footer import quantum_header, quantum_footer

quantum_header()
st.title("📘 Quantum Glossary")

st.markdown("""
Explore key quantum terms used across the Quantum Mentor app.  
Each definition is crafted for clarity and curiosity.
""")

glossary = {
    "Superposition": "A quantum system can exist in multiple states simultaneously.",
    "Entanglement": "Two particles remain connected, even when separated by large distances.",
    "Qubit": "The basic unit of quantum information, capable of being 0 and 1 at once.",
    "Quantum Tunneling": "Particles can pass through barriers they classically shouldn’t.",
    "Quantum Decoherence": "Loss of quantum behavior due to interaction with the environment."
}

for term, definition in glossary.items():
    st.subheader(f"🔹 {term}")
    st.markdown(f"{definition}")

quantum_footer()
