import json
import os


FILE = "data/last_response.json"



def save_last_response(question, answer):

    data = {
        "question": question,
        "answer": answer
    }

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )

    return "آخرین پاسخ ذخیره شد ✅"



def get_last_response():

    if not os.path.exists(FILE):
        return None

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)
