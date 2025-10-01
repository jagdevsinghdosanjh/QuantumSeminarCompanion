import streamlit as st
import json
import os

def quantum_header():
    st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <h1 style='color: #6C63FF;'>🧠 Quantum Mentor</h1>
        <p style='font-size: 1.1rem; color: #444;'>Empowering students through poetic science, modular logic, and quantum curiosity.</p>
        <hr style='border: none; height: 1px; background-color: #eee;'/>
    </div>
    """, unsafe_allow_html=True)

def quantum_footer(module_name="Quantum Core"):
    manifest_path = os.path.join(os.path.dirname(__file__), "footer_manifest.json")
    try:
        with open(manifest_path, "r") as f:
            manifest = json.load(f)
    except FileNotFoundError:
        manifest = {}

    poetic_line = manifest.get(module_name, {}).get("poetic_line", "Entangle your thoughts, collapse your doubts.")

    footer_html = f"""
        <hr style='border: none; height: 2px; background-color: green;'/>
        <div style='text-align: center; font-size: 0.9rem; color: #FFD700; padding-top: 1rem;'>
            <strong>{module_name}</strong><br/>
            <em>{poetic_line}</em><br/>
            <span style='font-size: 0.8rem; color:green;'>Powered by modular logic and poetic insight ⚛️</span>
        </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)


# def quantum_footer(module_name="Quantum Core"):
#     with open("footer_manifest.json") as f:
#         manifest = json.load(f)
#     poetic_line = manifest.get(module_name, {}).get("poetic_line", "Entangle your thoughts, collapse your doubts.")
    
#     footer_html = f"""
#         <hr style='border: none; height: 2px; background-color: #eee;'/>
#         <div style='text-align: center; font-size: 0.9rem; color: #FFD700; padding-top: 1rem;'>
#             <strong>{module_name}</strong><br/>
#             <em>{poetic_line}</em><br/>
#             <span style='font-size: 0.8rem; color: #aaa;'>Powered by modular logic and poetic insight ⚛️</span>
#         </div>
#     """
#     st.markdown(footer_html, unsafe_allow_html=True)


# def quantum_footer(module_name="Quantum Core", poetic_line="Entangle your thoughts, collapse your doubts."):
#     footer_html = f"""
#         <hr style='border: none; height: 2px; background-color: #eee;'/>
#         <div style='text-align: center; font-size: 0.9rem; color: #FFD700; padding-top: 1rem;'>
#             <strong>{module_name}</strong><br/>
#             <em>{poetic_line}</em><br/>
#             <span style='font-size: 0.8rem; color: #aaa;'>Powered by modular logic and poetic insight ⚛️</span>
#         </div>
#     """
#     st.markdown(footer_html, unsafe_allow_html=True)


# def quantum_footer():
#     st.markdown("""
#     <hr style='border: none; height: 2px; background-color: #eee;'/>
#     <div style='text-align: center; font-size: 0.9rem; border-color:black; color: yellow; padding-top: 1rem;'>
#         <p>“Let your imagination collapse into clarity.”</p>
#         <p>© 2025 Quantum Mentor · Designed by Jagdev Singh CF (GHS Chaananke Amritsar)</p>
#     </div>
#     """, unsafe_allow_html=True)

# def quantum_footer():
#     st.markdown("""
#         <hr style='border: none; height: 2px; background-color: #eee;'/>
#         <div style='text-align: center; font-size: 0.9rem; background-color:black; color: yellow; padding-top: 1rem;'>
#             Quantum insights powered by poetic logic ⚛️✨
#             <p>“Let your imagination collapse into clarity.”</p>
#         <p>© 2025 Quantum Mentor · Jagdev Singh CF (GHS Chaananke Amritsar)</p>
#         </div>
#     """, unsafe_allow_html=True)