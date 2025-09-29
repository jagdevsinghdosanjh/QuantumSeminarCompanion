import streamlit as st
from components.header_footer import quantum_header, quantum_footer

quantum_header()
st.title("🧠 Science Seminar Rubric")

st.markdown("""
This rubric helps evaluate student submissions for science seminars and hackathons.  
Each category is scored out of 10.
""")

st.markdown("""
| Category               | Description                                      |
|------------------------|--------------------------------------------------|
| Concept Clarity        | Is the quantum idea clearly explained?          |
| Creativity             | Are metaphors, visuals, or poetic elements used?|
| Technical Accuracy     | Is the science correct and well-researched?     |
| Presentation Quality   | Is the layout clean and engaging?               |
| Originality            | Is the idea unique and student-driven?          |
""")

st.info("Educators can adapt this rubric for classroom or event use.")

quantum_footer()
