def assign_badges(score, modules_completed):
    badges = []

    # Quiz performance badge
    if score >= 4:
        badges.append("🧠 Quantum Quiz Master")

    # Module completion badges
    if modules_completed >= 4:
        badges.append("🚀 Quantum Explorer")
    if modules_completed == 5:
        badges.append("🧙 Wisdom Wall Contributor")

    return badges

# def assign_badges(score, modules_completed):
#     badges = []

#     if score >= 4:
#         badges.append("🧠 Quantum Quiz Master")
#     if modules_completed >= 4:
#         badges.append("🚀 Quantum Explorer")
#     if modules_completed == 5:
#         badges.append("🧙 Wisdom Wall Contributor")

#     return badges
