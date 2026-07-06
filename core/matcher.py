# core/matcher.py (DISABLED - semantic mode active)

def similarity(text1, text2):
    return 0

def get_best_match(text, concepts):
    """
    پیدا کردن بهترین جواب از knowledge base
    """

    from core.knowledge import KNOWLEDGE_BASE

    best_score = 0
    best_answer = None

    print(f"[DEBUG TEXT]: '{text}'")

    for key, value in KNOWLEDGE_BASE.items():

        score = 0

        # تطبیق ساده متنی
        if key in text:
            score += 1

        # اگر concept ها مشترک بودن
        if hasattr(value, "concepts"):
            if concepts & set(value.concepts):
                score += 2

        print(f"[DEBUG MATCH] key={key} | score={score}")

        if score > best_score:
            best_score = score
            best_answer = value.answer if hasattr(value, "answer") else value

    if best_score == 0:
        return None

    print(f"[Knowledge Score]: {best_score}")
    return best_answer
