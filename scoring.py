import random

def calculate_score(confidence):

    base = int(confidence * 100)

    variability = random.randint(-20, 20)

    score = max(30, min(98, base + variability))

    if score > 80:
        urgency = "High"
    elif score > 60:
        urgency = "Medium"
    else:
        urgency = "Low"

    return score, urgency
