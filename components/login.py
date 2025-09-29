import streamlit as st

def student_login():
    st.sidebar.markdown("### 👤 Student Login")
    name = st.sidebar.text_input("Enter your name")
    if name:
        st.session_state["student_name"] = name
        st.sidebar.success(f"Welcome, {name}!")
