def calculate_confidence(score):

    """
    تبدیل امتیاز مهارت به عدد بین 0 و 1
    """

    score = max(0, min(score, 100))

    return score / 100


def get_confidence(score):

    confidence = calculate_confidence(score)

    if confidence >= 0.8:
        return "high"

    if confidence >= 0.5:
        return "medium"

    return "low"


def should_use_memory(score):

    confidence = get_confidence(score)

    print("[CONFIDENCE]", confidence)

    return confidence == "high"
