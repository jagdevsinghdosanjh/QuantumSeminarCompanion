import streamlit as st
import json
import os
import re
from components.quantum_card import quantum_mentor_avatar
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("📚 Quantum Explorer")
quantum_mentor_avatar()

st.markdown("""
Welcome to the Quantum Explorer.  
Here, you’ll decode key quantum concepts through definitions, diagrams, and poetic metaphors.  
Select a concept below to begin your journey.
""")

# Load glossary safely
try:
    with open("data/glossary.json", "r") as f:
        glossary = json.load(f)
except FileNotFoundError:
    st.error("Glossary file not found. Using default glossary.")
    glossary = {
        "Superposition": "A quantum system can exist in multiple states simultaneously.",
        "Entanglement": "Two particles remain connected, even when separated by large distances.",
        "Qubit": "The basic unit of quantum information, capable of being 0 and 1 at once.",
        "Quantum Tunneling": "A particle's ability to pass through barriers it classically shouldn't cross.",
        "Quantum Decoherence": "Loss of quantum behavior due to interaction with the environment.",
        "Measurement": "The act of observing a quantum system, collapsing its superposition into a definite state.",
        "Quantum Interference": "The overlapping of quantum states, where probabilities amplify or cancel each other.",
        "Wavefunction": "A mathematical description of a quantum system’s state and its probability distribution.",
        "Quantum Gate": "An operation that changes the state of qubits, analogous to logic gates in classical computing.",
        "Bell's Theorem": "A foundational result showing that no local hidden variables can explain quantum correlations.",
        "No-Cloning Theorem": "A principle stating that unknown quantum states cannot be copied perfectly.",
        "Quantum Supremacy": "The point at which a quantum computer outperforms the best classical counterpart on a specific task.",
        "Quantum Error Correction": "Techniques to protect quantum information from decoherence and noise.",
        "Quantum Algorithm": "A set of quantum operations designed to solve problems faster than classical algorithms.",
        "Quantum Cryptography": "Securing communication using quantum principles, making eavesdropping detectable."
    }
except json.JSONDecodeError:
    st.error("Glossary file is corrupted or improperly formatted.")
    glossary = {}

# Concept selector
if glossary:
    concept = st.selectbox("🔍 Choose a quantum concept", sorted(glossary.keys()))

    if concept:
        st.subheader(f"🧠 {concept}")
        st.markdown(f"**Definition:** {glossary[concept]}")

        # Metaphorical insight
        metaphors = {
            "Superposition": "🌌 Like a coin spinning in mid-air—both heads and tails until it lands.",
            "Entanglement": "🔗 Two dancers moving in sync, even from different continents.",
            "Qubit": "⚛️ A whisper between 0 and 1, never fully choosing sides.",
            "Quantum Tunneling": "🚪 A ghost walking through a locked door.",
            "Quantum Decoherence": "🌫️ A dream fading as the sun rises—quantum magic lost to reality.",
            "Measurement": "🎯 Like catching a butterfly—once observed, its flight path is fixed.",
            "Quantum Interference": "🎭 A chorus of possibilities, some harmonizing, others silenced.",
            "Wavefunction": "🌊 A shimmering map of maybes, flowing through probability space.",
            "Quantum Gate": "🧮 A twist in the quantum dance, reshaping the rhythm of qubits.",
            "Bell's Theorem": "🔍 A cosmic detective story—no local clues explain the spooky sync.",
            "No-Cloning Theorem": "📵 A quantum selfie that can’t be duplicated.",
            "Quantum Supremacy": "🚀 A leap beyond classical limits—where quantum speed reigns.",
            "Quantum Error Correction": "🛡️ A spell of protection against the noise of reality.",
            "Quantum Algorithm": "🧩 A puzzle-solving spell cast in quantum logic.",
            "Quantum Cryptography": "🔐 A whisper shielded by quantum truth—safe from prying ears."
        }

        if concept in metaphors:
            st.markdown(f"**Metaphor:** *{metaphors[concept]}*")
        else:
            st.info("Metaphor not yet available—submit your poetic insight!")

        # Optional diagram
        sanitized_name = re.sub(r"[^\w]", "_", concept.lower())
        image_path = f"assets/diagrams/{sanitized_name}.png"
        if os.path.exists(image_path):
            st.image(image_path, caption=f"{concept} Diagram", use_container_width=True)
        else:
            st.info("Diagram not available for this concept.")

quantum_footer()


# import streamlit as st
# import json
# from components.quantum_card import quantum_mentor_avatar
# import os
# from components.header_footer import quantum_header, quantum_footer

# quantum_header()

# st.title("📚 Quantum Explorer")
# quantum_mentor_avatar()

# st.markdown("""
# Welcome to the Quantum Explorer.  
# Here, you’ll decode key quantum concepts through definitions, diagrams, and poetic metaphors.  
# Select a concept below to begin your journey.
# """)

# # Load glossary safely
# try:
#     with open("data/glossary.json", "r") as f:
#         glossary = json.load(f)
# except FileNotFoundError:
#     st.error("Glossary file not found. Using default glossary.")
#     glossary = {
#         "Superposition": "A quantum system can exist in multiple states simultaneously.",
#         "Entanglement": "Two particles remain connected, even when separated by large distances.",
#         "Qubit": "The basic unit of quantum information, capable of being 0 and 1 at once.",
#         "Quantum Tunneling": "Particles can pass through barriers they classically shouldn’t.",
#         "Quantum Decoherence": "Loss of quantum behavior due to interaction with the environment."
#     }
# except json.JSONDecodeError:
#     st.error("Glossary file is corrupted or improperly formatted.")
#     glossary = {}

# # Concept selector
# if glossary:
#     concept = st.selectbox("🔍 Choose a quantum concept", list(glossary.keys()))

#     if concept:
#         st.subheader(f"🧠 {concept}")
#         st.markdown(f"**Definition:** {glossary[concept]}")

#         # Metaphorical insight
#         metaphors = {
#             "Superposition": "🌌 Like a coin spinning in mid-air—both heads and tails until it lands.",
#             "Entanglement": "🔗 Two dancers moving in sync, even from different continents.",
#             "Qubit": "⚛️ A whisper between 0 and 1, never fully choosing sides.",
#             "Quantum Tunneling": "🚪 A ghost walking through a locked door.",
#             "Quantum Decoherence": "🌫️ A dream fading as the sun rises—quantum magic lost to reality."
#         }

#         if concept in metaphors:
#             st.markdown(f"**Metaphor:** *{metaphors[concept]}*")

#         # Optional diagram
#         image_path = f"assets/diagrams/{concept.lower().replace(' ', '_')}.png"
#         if os.path.exists(image_path):
#             st.image(image_path, caption=f"{concept} Diagram", use_container_width=True)
#         else:
#             st.info("Diagram not available for this concept.")

# quantum_footer()

# # import streamlit as st
# # import json
# # from components.quantum_card import quantum_mentor_avatar

# # st.title("📚 Quantum Explorer")
# # quantum_mentor_avatar()

# # st.markdown("""
# # Welcome to the Quantum Explorer.  
# # Here, you’ll decode key quantum concepts through definitions, diagrams, and poetic metaphors.  
# # Select a concept below to begin your journey.
# # """)

# # # Load glossary safely
# # try:
# #     with open("data/glossary.json", "r") as f:
# #         glossary = json.load(f)
# # except FileNotFoundError:
# #     st.error("Glossary file not found. Using default glossary.")
# #     glossary = {
# #         "Superposition": "A quantum system can exist in multiple states simultaneously.",
# #         "Entanglement": "Two particles remain connected, even when separated by large distances.",
# #         "Qubit": "The basic unit of quantum information, capable of being 0 and 1 at once.",
# #         "Quantum Tunneling": "Particles can pass through barriers they classically shouldn’t.",
# #         "Quantum Decoherence": "Loss of quantum behavior due to interaction with the environment."
# #     }
# # except json.JSONDecodeError:
# #     st.error("Glossary file is corrupted or improperly formatted.")
# #     glossary = {}

# # # Concept selector
# # if glossary:
# #     concept = st.selectbox("🔍 Choose a quantum concept", list(glossary.keys()))

# #     if concept:
# #         st.subheader(f"🧠 {concept}")
# #         st.markdown(f"**Definition:** {glossary[concept]}")

# #         # Metaphorical insight
# #         metaphors = {
# #             "Superposition": "🌌 Like a coin spinning in mid-air—both heads and tails until it lands.",
# #             "Entanglement": "🔗 Two dancers moving in sync, even from different continents.",
# #             "Qubit": "⚛️ A whisper between 0 and 1, never fully choosing sides.",
# #             "Quantum Tunneling": "🚪 A ghost walking through a locked door.",
# #             "Quantum Decoherence": "🌫️ A dream fading as the sun rises—quantum magic lost to reality."
# #         }

# #         if concept in metaphors:
# #             st.markdown(f"**Metaphor:** *{metaphors[concept]}*")

# #         # Optional diagram
# #         image_path = f"assets/diagrams/{concept.lower().replace(' ', '_')}.png"
# #         try:
# #             st.image(image_path, caption=f"{concept} Diagram", use_column_width=True)
# #         except FileNotFoundError:
# #             st.info("Diagram not available for this concept.")

# # # import streamlit as st
# # # import json
# # # from components.quantum_card import quantum_mentor_avatar

# # # st.title("📚 Quantum Explorer")
# # # quantum_mentor_avatar()

# # # st.markdown("""
# # # Welcome to the Quantum Explorer.  
# # # Here, you’ll decode key quantum concepts through definitions, diagrams, and poetic metaphors.  
# # # Select a concept below to begin your journey.
# # # """)

# # # # Load glossary
# # # try:
# # #     with open("data/glossary.json", "r") as f:
# # #         glossary = json.load(f)
# # # except:
# # #     glossary = {
# # #         "Superposition": "A quantum system can exist in multiple states simultaneously.",
# # #         "Entanglement": "Two particles remain connected, even when separated by large distances.",
# # #         "Qubit": "The basic unit of quantum information, capable of being 0 and 1 at once.",
# # #         "Quantum Tunneling": "Particles can pass through barriers they classically shouldn’t.",
# # #         "Quantum Decoherence": "Loss of quantum behavior due to interaction with the environment."
# # #     }

# # # # Concept selector
# # # concept = st.selectbox("🔍 Choose a quantum concept", list(glossary.keys()))

# # # if concept:
# # #     st.subheader(f"🧠 {concept}")
# # #     st.markdown(f"**Definition:** {glossary[concept]}")

# # #     # Metaphorical insight
# # #     metaphors = {
# # #         "Superposition": "🌌 Like a coin spinning in mid-air—both heads and tails until it lands.",
# # #         "Entanglement": "🔗 Two dancers moving in sync, even from different continents.",
# # #         "Qubit": "⚛️ A whisper between 0 and 1, never fully choosing sides.",
# # #         "Quantum Tunneling": "🚪 A ghost walking through a locked door.",
# # #         "Quantum Decoherence": "🌫️ A dream fading as the sun rises—quantum magic lost to reality."
# # #     }

# # #     if concept in metaphors:
# # #         st.markdown(f"**Metaphor:** *{metaphors[concept]}*")

# # #     # Optional diagram placeholder
# # #     st.image(f"assets/diagrams/{concept.lower().replace(' ', '_')}.png", caption=f"{concept} Diagram", use_column_width=True)
