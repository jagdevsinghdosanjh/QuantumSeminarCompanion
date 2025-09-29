import streamlit as st
import json
from random import shuffle
from components.header_footer import quantum_header, quantum_footer

quantum_header()

st.title("📚 Quantum Quiz")
st.markdown("Test your understanding of quantum concepts. Select the best answer for each question.")

# Load and shuffle questions once
if "questions" not in st.session_state:
    with open("data/quantum_questions.json", "r") as f:
        questions = json.load(f)
    shuffle(questions)
    st.session_state.questions = questions[:15]
    st.session_state.answers = [None] * 15
    st.session_state.submitted = [False] * 15
    st.session_state.score = 0

# Display questions
for i, q in enumerate(st.session_state.questions):
    st.subheader(f"Q{i+1}: {q['question']}")
    selected = st.radio("Choose one:", q["options"], key=f"radio_{i}")

    if not st.session_state.submitted[i]:
        if st.button(f"Submit Q{i+1}", key=f"btn_{i}"):
            correct = q["options"][q["answer"][0]]
            st.session_state.answers[i] = selected
            st.session_state.submitted[i] = True
            if selected == correct:
                st.success("✅ Correct!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect. Correct answer: {correct}")
            st.info(f"🧠 Explanation: {q['explanation']}")
    else:
        correct = q["options"][q["answer"][0]]
        if st.session_state.answers[i] == correct:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. Correct answer: {correct}")
        st.info(f"🧠 Explanation: {q['explanation']}")

# Final score
if all(st.session_state.submitted):
    st.markdown("---")
    st.success(f"🎯 Final Score: {st.session_state.score}/15")

quantum_footer()

# import streamlit as st
# import json
# from random import shuffle
# from components.header_footer import quantum_header, quantum_footer

# quantum_header()

# st.title("📚 Quantum Quiz")
# st.markdown("Test your understanding of quantum concepts. Select the best answer for each question.")

# # Load and shuffle questions once
# if "questions" not in st.session_state:
#     with open("data/quantum_questions.json", "r") as f:
#         questions = json.load(f)
#     shuffle(questions)
#     st.session_state.questions = questions[:15]
#     st.session_state.answers = [None] * 5
#     st.session_state.submitted = [False] * 5
#     st.session_state.score = 0

# # Display questions
# for i, q in enumerate(st.session_state.questions):
#     st.subheader(f"Q{i+1}: {q['question']}")
#     selected = st.radio("Choose one:", q["options"], key=f"radio_{i}")
    
#     if not st.session_state.submitted[i]:
#         if st.button(f"Submit Q{i+1}", key=f"btn_{i}"):
#             correct = q["options"][q["answer"][0]]
#             st.session_state.answers[i] = selected
#             st.session_state.submitted[i] = True
#             if selected == correct:
#                 st.success("✅ Correct!")
#                 st.session_state.score += 1
#             else:
#                 st.error(f"❌ Incorrect. Correct answer: {correct}")
#             st.info(f"🧠 Explanation: {q['explanation']}")
#     else:
#         correct = q["options"][q["answer"][0]]
#         if st.session_state.answers[i] == correct:
#             st.success("✅ Correct!")
#         else:
#             st.error(f"❌ Incorrect. Correct answer: {correct}")
#         st.info(f"🧠 Explanation: {q['explanation']}")

# # Final score
# if all(st.session_state.submitted):
#     st.markdown("---")
#     st.success(f"🎯 Final Score: {st.session_state.score}/5")

# quantum_footer()

# # import streamlit as st
# # import json
# # from random import shuffle
# # from components.header_footer import quantum_header, quantum_footer

# # quantum_header()

# # # Load questions
# # with open("data/quantum_questions.json", "r") as f:
# #     questions = json.load(f)

# # st.title("📚 Quantum Quiz")
# # st.markdown("Test your understanding of quantum concepts. Select the best answer for each question.")

# # score = 0
# # shuffle(questions)

# # for i, q in enumerate(questions[:5]):
# #     st.subheader(f"Q{i+1}: {q['question']}")
# #     selected = st.radio("Choose one:", q["options"], key=i)
# #     if st.button(f"Submit Q{i+1}", key=f"btn{i}"):
# #         correct = q["options"][q["answer"][0]]
# #         if selected == correct:
# #             st.success("✅ Correct!")
# #             score += 1
# #         else:
# #             st.error(f"❌ Incorrect. Correct answer: {correct}")
# #         st.info(f"🧠 Explanation: {q['explanation']}")

# # st.markdown("---")
# # st.write(f"🎯 Final Score: {score}/5")

# # quantum_footer()

