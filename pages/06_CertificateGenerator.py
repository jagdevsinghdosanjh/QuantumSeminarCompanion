import streamlit as st
from utils.badge_engine import assign_badges
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("🎓 Quantum Mentor Certificate")
st.markdown("Complete all modules and earn your personalized certificate!")

name = st.text_input("Enter your full name")
score = st.slider("Your Quiz Score (out of 5)", 0, 5, 3)
modules_completed = st.slider("Modules Completed", 0, 5, 3)

if name and st.button("Generate Certificate"):
    badges = assign_badges(score, modules_completed)
    st.success(f"🎉 Congratulations, {name}!")
    st.markdown("You've earned the following badges:")
    for badge in badges:
        st.markdown(f"- {badge}")

    st.markdown("---")
    st.markdown(f"""
    🧾 **Certificate of Completion**  
    This certifies that **{name}** has successfully completed the Quantum Mentor program  
    with a score of {score}/5 and full engagement across {modules_completed} modules.  
    Keep exploring, keep questioning, and keep collapsing possibilities into brilliance.
    """)

# Your page content here...

quantum_footer()