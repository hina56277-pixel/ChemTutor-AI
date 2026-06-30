def router(question):
    question = question.lower()

    if any(word in question for word in ["balance", "equation"]):
        return "Equation Agent"

    elif any(word in question for word in ["mechanism", "sn1", "sn2", "reaction"]):
        return "Mechanism Agent"

    elif any(word in question for word in ["calculate", "mole", "mass", "numerical"]):
        return "Numerical Agent"

    else:
        return "Theory Agent"
