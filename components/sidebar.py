import streamlit as st

def render_sidebar():
    # Glowing title
    st.sidebar.markdown("""
    <h2 style='color:#6C63FF; text-align:center;'>🔮 Quantum Mentor</h2>
    <p style='text-align:center; font-size:0.9rem; color:#888;'>Navigate through modules:</p>
    """, unsafe_allow_html=True)

    # 🧭 Core Modules
    st.sidebar.markdown("<h4 style='color:#00C2CB;'>🧭 Core Modules</h4>", unsafe_allow_html=True)
    st.sidebar.page_link("pages/01_Home.py", label="🏠 Home")
    st.sidebar.page_link("pages/02_QuantumLogicSimulator.py", label="🧠 Quantum Logic Simulator")
    st.sidebar.page_link("pages/03_QuantumQuiz.py", label="📚 Quantum Quiz")
    st.sidebar.page_link("pages/04_HackathonHelper.py", label="🚀 Hackathon Helper")
    st.sidebar.page_link("pages/05_QuantumWisdomWall.py", label="🧙 Quantum Wisdom Wall")

    # Gradient divider
    st.sidebar.markdown("""
    <hr style='border:none; height:3px; background:linear-gradient(to right, #6C63FF, #00C2CB);'/>
    """, unsafe_allow_html=True)

    # Seminar Info
    st.sidebar.markdown("""
    <div style='font-size:0.85rem; color:Green; text-align:center;'>
    Built for students of Classes VIII–X<br>
    Inspired by the <b>Quantum Age Begins</b> Seminar
    </div>
    """, unsafe_allow_html=True)

    # 🎓 Student Tools
    st.sidebar.markdown("<h4 style='color:#00C2CB;'>🎓 Student Tools</h4>", unsafe_allow_html=True)
    st.sidebar.page_link("pages/06_CertificateGenerator.py", label="🎓 Certificate Generator")
    st.sidebar.page_link("pages/07_Leaderboard.py", label="🏆 Leaderboard")
    st.sidebar.page_link("pages/11_PrintableSummary.py", label="🧾 Printable Summary")

    # Gradient divider
    st.sidebar.markdown("""
    <hr style='border:none; height:3px; background:linear-gradient(to right, #FFD700, #00C2CB);'/>
    """, unsafe_allow_html=True)

    # 🧑‍🏫 Educator Dashboards
    st.sidebar.markdown("<h4 style='color:#00C2CB;'>🧑‍🏫 Educator Dashboards</h4>", unsafe_allow_html=True)
    st.sidebar.page_link("pages/08_ContributorDashboard.py", label="🧑‍🏫 Contributor Dashboard")
    st.sidebar.page_link("pages/09_ChallengeDashboard.py", label="🎮 Mentor Challenge")
    st.sidebar.page_link("pages/10_ChallengeWeek.py", label="📅 Challenge Week")
    st.sidebar.page_link("pages/12_SchoolDashboard.py", label="🏫 School Dashboard")

# import streamlit as st

# def render_sidebar():
#     st.sidebar.title("🔮 Quantum Mentor")
#     st.sidebar.markdown("Navigate through modules:")

#     # 🧭 Core Modules
#     st.sidebar.page_link("pages/01_Home.py", label="🏠 Home")
#     st.sidebar.page_link("pages/02_QuantumLogicSimulator.py", label="🧠 Quantum Logic Simulator")
#     st.sidebar.page_link("pages/03_QuantumQuiz.py", label="📚 Quantum Quiz")
#     st.sidebar.page_link("pages/04_HackathonHelper.py", label="🚀 Hackathon Helper")
#     st.sidebar.page_link("pages/05_QuantumWisdomWall.py", label="🧙 Quantum Wisdom Wall")
#     st.sidebar.markdown("---")
#     st.sidebar.info("Built for students of Classes VIII–X\nInspired by the Quantum Age Begins Seminar")

#     # 🎓 Student Tools
#     st.sidebar.page_link("pages/06_CertificateGenerator.py", label="🎓 Certificate Generator")
#     st.sidebar.page_link("pages/07_Leaderboard.py", label="🏆 Leaderboard")
#     st.sidebar.page_link("pages/11_PrintableSummary.py", label="🧾 Printable Summary")

#     st.sidebar.markdown("---")

#     # 🧑‍🏫 Educator Dashboards
#     st.sidebar.page_link("pages/08_ContributorDashboard.py", label="🧑‍🏫 Contributor Dashboard")
#     st.sidebar.page_link("pages/09_ChallengeDashboard.py", label="🎮 Mentor Challenge")
#     st.sidebar.page_link("pages/10_ChallengeWeek.py", label="📅 Challenge Week")
#     st.sidebar.page_link("pages/12_SchoolDashboard.py", label="🏫 School Dashboard")


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
