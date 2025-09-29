import random

def superposition_decision(options):
    """
    Simulates quantum-style decision making by assigning normalized probabilities
    to a list of options using random weights.
    """
    if not options or len(options) < 2:
        raise ValueError("At least two options are required for superposition.")

    weights = [random.random() for _ in options]
    total = sum(weights)
    probabilities = [round(w / total, 2) for w in weights]
    return dict(zip(options, probabilities))


# import random

# def superposition_decision(options):
#     weights = [random.random() for _ in options]
#     total = sum(weights)
#     probabilities = [round(w / total, 2) for w in weights]
#     return dict(zip(options, probabilities))

# def superposition_decision(options):
#     import random
#     weights = [random.random() for _ in options]
#     total = sum(weights)
#     probabilities = [round(w / total, 2) for w in weights]
#     return dict(zip(options, probabilities))