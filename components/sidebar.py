import streamlit as st

def render_sidebar():
    st.sidebar.title("🔮 Quantum Mentor")
    st.sidebar.markdown("Navigate through modules:")

    # 🧭 Core Modules
    st.sidebar.page_link("pages/01_Home.py", label="🏠 Home")
    st.sidebar.page_link("pages/02_QuantumLogicSimulator.py", label="🧠 Quantum Logic Simulator")
    st.sidebar.page_link("pages/03_QuantumQuiz.py", label="📚 Quantum Quiz")
    st.sidebar.page_link("pages/04_HackathonHelper.py", label="🚀 Hackathon Helper")
    st.sidebar.page_link("pages/05_QuantumWisdomWall.py", label="🧙 Quantum Wisdom Wall")
    st.sidebar.markdown("---")
    st.sidebar.info("Built for students of Classes VIII–X\nInspired by the Quantum Age Begins Seminar")

    # 🎓 Student Tools
    st.sidebar.page_link("pages/06_CertificateGenerator.py", label="🎓 Certificate Generator")
    st.sidebar.page_link("pages/07_Leaderboard.py", label="🏆 Leaderboard")
    st.sidebar.page_link("pages/11_PrintableSummary.py", label="🧾 Printable Summary")

    st.sidebar.markdown("---")

    # 🧑‍🏫 Educator Dashboards
    st.sidebar.page_link("pages/08_ContributorDashboard.py", label="🧑‍🏫 Contributor Dashboard")
    st.sidebar.page_link("pages/09_ChallengeDashboard.py", label="🎮 Mentor Challenge")
    st.sidebar.page_link("pages/10_ChallengeWeek.py", label="📅 Challenge Week")
    st.sidebar.page_link("pages/12_SchoolDashboard.py", label="🏫 School Dashboard")


# import streamlit as st

# def render_sidebar():
#     st.sidebar.title("🔮 Quantum Mentor")
#     st.sidebar.markdown("Navigate through modules:")
#     st.sidebar.page_link("pages/01_Home.py", label="🏠 Home")
#     st.sidebar.page_link("pages/02_QuantumLogicSimulator.py", label="🧠 Quantum Logic Simulator")
#     st.sidebar.page_link("pages/03_QuantumQuiz.py", label="📚 Quantum Quiz")
#     st.sidebar.page_link("pages/04_HackathonHelper.py", label="🚀 Hackathon Helper")
#     st.sidebar.markdown("---")
#     st.sidebar.info("Built for students of Classes VIII–X\nInspired by the Quantum Age Begins Seminar")
#     st.sidebar.page_link("pages/05_QuantumWisdomWall.py", label="🧙 Quantum Wisdom Wall")
#     st.sidebar.page_link("pages/06_CertificateGenerator.py", label="🎓 Certificate Generator")
#     st.sidebar.page_link("pages/07_Leaderboard.py", label="🏆 Leaderboard")
#     st.sidebar.page_link("pages/08_ContributorDashboard.py", label="🧑‍🏫 Contributor Dashboard")
#     st.sidebar.page_link("pages/09_ChallengeDashboard.py", label="🎮 Mentor Challenge")
#     st.sidebar.page_link("pages/10_ChallengeWeek.py", label="📅 Challenge Week")
#     st.sidebar.page_link("pages/11_PrintableSummary.py", label="🧾 Printable Summary")
#     st.sidebar.page_link("pages/12_SchoolDashboard.py", label="🏫 School Dashboard")
