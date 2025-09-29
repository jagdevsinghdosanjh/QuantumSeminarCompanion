import streamlit as st
from components.quantum_card import quantum_mentor_avatar
from utils.logic_engine import superposition_decision
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("🧠 Quantum Logic Simulator")
quantum_mentor_avatar()

st.markdown("""
Welcome to the Quantum Logic Simulator.  
Here, decisions are not binary—they exist in superposition.  
Enter your options below, and let quantum reasoning reveal the hidden probabilities.
""")

# Input options
options_input = st.text_area("🔍 Enter your choices (comma-separated)", "Physics, Biology, Computer Science")

if options_input:
    options = [opt.strip() for opt in options_input.split(",") if opt.strip()]
    if len(options) >= 2:
        st.subheader("🔮 Quantum Probabilities")
        result = superposition_decision(options)
        for opt, prob in result.items():
            st.write(f"• **{opt}** → {prob * 100:.1f}% chance")
    else:
        st.warning("Please enter at least two options.")
quantum_footer()

# import streamlit as st
# from components.quantum_card import quantum_mentor_avatar
# from utils.logic_engine import superposition_decision

# st.title("🧠 Quantum Logic Simulator")
# quantum_mentor_avatar()

# st.markdown("""
# Welcome to the Quantum Logic Simulator.  
# Here, decisions are not binary—they exist in superposition.  
# Enter your options below, and let quantum reasoning reveal the hidden probabilities.
# """)

# # Input options
# options_input = st.text_area("🔍 Enter your choices (comma-separated)", "Physics, Biology, Computer Science")

# if options_input:
#     options = [opt.strip() for opt in options_input.split(",") if opt.strip()]
#     if len(options) >= 2:
#         st.subheader("🔮 Quantum Probabilities")
#         result = superposition_decision(options)
#         for opt, prob in result.items():
#             st.write(f"• **{opt}** → {prob * 100:.1f}% chance")
#     else:
#         st.warning("Please enter at least two options.")

# st.title("🧠 Quantum Logic Simulator")
# quantum_mentor_avatar()

# st.markdown("""
# Welcome to the Quantum Logic Simulator.  
# Here, decisions are not binary—they exist in superposition.  
# Choose your options, and let quantum reasoning guide your path.
# """)
