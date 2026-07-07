# core/knowledge.py

import json
from core.matcher import similarity

KNOWLEDGE_FILE = "data/knowledge.json"


# ---------- Load Knowledge ----------
def load_knowledge():
    try:
        with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}


# ---------- Save Knowledge ----------
def save_knowledge(data):
    with open(KNOWLEDGE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# ---------- Find Best Match ----------
def search_knowledge(text):
    data = load_knowledge()

    best_key = None
    best_score = 0

    print(f"[AFTER NORMALIZE]: '{text}'")

    for key in data.keys():
        score = similarity(text, key)
        print(f"[DEBUG MATCH] key={key} | score={score}")

        if score > best_score:
            best_score = score
            best_key = key

    print(f"[Knowledge Score]: {best_score} ({best_key})")

    # ---------- IMPORTANT RULE ----------
    # فقط اگر match واقعی داشتیم جواب بده
    if best_key and best_score >= 2:
        return data[best_key]

    return None


# ---------- Learn New Thing ----------
def learn_knowledge(text):
    data = load_knowledge()

    if text in data:
        return False

    data[text] = "این مورد را هنوز یاد نگرفتم"
    save_knowledge(data)
    return True
