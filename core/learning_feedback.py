import json
import os


FILE = "data/ai_feedback.json"



def save_feedback(question, answer, feedback):

    data = []

    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)


    item = {
        "question": question,
        "answer": answer,
        "feedback": feedback
    }


    data.append(item)


    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


    return "بازخورد ذخیره شد ✅"



def get_feedback():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)
