def check_challenge_completion(user_data):
    completed = []

    if user_data.get("quiz_score", 0) >= 4:
        completed.append("Quantum Quiz")
    if user_data.get("wisdom_submitted", False):
        completed.append("Wisdom Wall")
    if user_data.get("used_simulator", False):
        completed.append("Logic Simulator")
    if user_data.get("visited_helper", False):
        completed.append("Hackathon Helper")
    if user_data.get("certificate_generated", False):
        completed.append("Certificate")

    return completed
