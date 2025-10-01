import streamlit as st

def quantum_header():
    st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <h1 style='color: #6C63FF;'>🧠 Quantum Mentor</h1>
        <p style='font-size: 1.1rem; color: #444;'>Empowering students through poetic science, modular logic, and quantum curiosity.</p>
        <hr style='border: none; height: 1px; background-color: #eee;'/>
    </div>
    """, unsafe_allow_html=True)

def quantum_footer():
    st.markdown("""
        <hr style='border: none; height: 2px; background-color: #eee;'/>
        <div style='text-align: center; font-size: 0.9rem; background-color:black; color: yellow; padding-top: 1rem;'>
            Quantum insights powered by poetic logic ⚛️✨
        </div>
    """, unsafe_allow_html=True)