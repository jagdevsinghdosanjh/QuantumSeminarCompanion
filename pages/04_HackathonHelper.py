import streamlit as st
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("🚀 Hackathon Helper")
st.markdown("""
Welcome to the Hackathon Helper.  
This space is designed to guide you through quantum-themed challenges, spark ideas, and help you prepare for science seminars and innovation events.
""")

st.subheader("🎯 Challenge Tracks")
st.markdown("""
Choose a track that resonates with your curiosity:

- **Quantum Logic & Simulation**  
  Build tools that simulate quantum decisions or entanglement.

- **Poetic Science Communication**  
  Craft metaphors, riddles, or visual stories that explain quantum concepts.

- **Eco-Innovation with Quantum Thinking**  
  Apply quantum principles to sustainability, energy, or climate solutions.

- **Student Dashboard Design**  
  Create intuitive interfaces for tracking quiz scores, badges, and reflections.

- **Wisdom Wall Expansion**  
  Design modules that collect and showcase student insights creatively.
""")

st.subheader("🧠 Mentor Tips")
st.markdown("""
- Start with a concept you love—then build outward.  
- Use metaphors, visuals, and interactivity to make your idea shine.  
- Keep your solution modular and reproducible.  
- Document your process clearly—others will learn from your clarity.  
- Honor originality, teamwork, and curiosity.
""")
# st.subheader("📦 Starter Resources")
# st.markdown("""
# - 📘 [Quantum Glossary](05_QuantumGlossary.py)  
# - 🏅 [Badge Tracker](06_BadgeTrackerTemplate.py)  
# - 🧠 [Science Seminar](07_ScienceSeminarRubric.py)  
# - 🔧 [Streamlit Component Guide](https://docs.streamlit.io)
# """)

st.subheader("📦 Starter Resources")
st.markdown("""
- [Streamlit Component Guide](https://docs.streamlit.io) 
- [Your thoughts create Reality](https://youtu.be/19-QUNqsGJQ)  
- [How Actully Reflection works at Quantum Level](https://youtu.be/0u7m7YjnfJw)  
- [5 Facts about Quantum Thought](https://youtu.be/DUA0VqfSsf8)
""")

st.info("Ready to build? Ask your mentor for a challenge prompt or start prototyping below.")

quantum_footer()
