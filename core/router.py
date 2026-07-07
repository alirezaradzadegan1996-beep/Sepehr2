# core/router.py

from core.knowledge import load_knowledge, learn_knowledge
from core.concept import extract_concepts


# ---------- MAIN ROUTE ----------
def route(text):

    print(f"DEBUG TEXT: '{text}'")
    print("DEBUG INTENT: knowledge")

    # استخراج مفهوم‌ها
    text_concepts = extract_concepts(text)
    print(f"[CONCEPTS INPUT]: {text_concepts}")

    data = load_knowledge()

    best_key = None
    best_score = 0

    # مقایسه مفهومی
    for key in data.keys():

        key_concepts = extract_concepts(key)

        score = len(text_concepts & key_concepts)

        print(f"[DEBUG MATCH] key={key} | concepts={key_concepts} | score={score}")

        if score > best_score:
            best_score = score
            best_key = key

    print(f"[Knowledge Score]: {best_score} ({best_key})")

    # تصمیم نهایی

    if best_key and best_score >= 2:
        return data[best_key]

    # اگر چیزی پیدا نشد → یادگیری
    print("سپهر: این مورد را هنوز یاد نگرفتم ❌")
    learn_knowledge(text)

    return None
