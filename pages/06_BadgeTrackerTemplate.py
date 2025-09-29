import streamlit as st
import pandas as pd
from components.header_footer import quantum_header, quantum_footer

quantum_header()
st.title("🏅 Quantum Mentor Badge Tracker")

st.markdown("""
Track student progress across core modules:  
- 🧠 Quantum Explorer  
- 📚 Quantum Quiz  
- 🧙 Wisdom Wall  
- 🎮 Challenge Week  
- 🎓 Certificate Generator
""")

# Sample student data
data = {
    "Student Name": ["Aditi", "Rohan", "Meera", "Kabir", "Simran"],
    "Quantum Explorer": [True, True, True, False, True],
    "Quantum Quiz": [True, True, True, True, False],
    "Wisdom Wall": [True, False, True, False, True],
    "Challenge Week": [True, False, True, True, False],
    "Certificate": [True, False, True, False, False]
}

df = pd.DataFrame(data)

# Convert boolean to emoji for display
emoji_df = df.copy()
for col in df.columns[1:]:
    emoji_df[col] = df[col].apply(lambda x: "✅" if x else "❌")

st.dataframe(emoji_df, width='stretch')

# st.dataframe(emoji_df, use_container_width=True)

st.markdown("---")
st.info("Educators can export this table to Excel or Google Sheets for real-time tracking and badge assignment.")

quantum_footer()


# import streamlit as st
# from components.header_footer import quantum_header, quantum_footer

# quantum_header()
# st.title("🏅 Badge Tracker Template")

# st.markdown("""
# Use this template to track student progress across modules:  
# - Quantum Explorer  
# - Quantum Quiz  
# - Wisdom Wall  
# - Challenge Week  
# - Certificate Generator
# """)

# st.markdown("""
# | Student Name | Explorer | Quiz | Wisdom Wall | Challenge Week | Certificate |
# |--------------|----------|------|-------------|----------------|-------------|
# | Aditi        | ✅       | ✅   | ✅          | ✅             | ✅          |
# | Rohan        | ✅       | ✅   | ❌          | ❌             | ❌          |
# | Meera        | ✅       | ✅   | ✅          | ✅             | ✅          |
# """)

# st.info("Educators can copy this into Excel or Google Sheets and customize it for their classroom.")

# quantum_footer()
