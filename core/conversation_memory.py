import json
import os
from datetime import datetime


FILE = "data/history.json"



def load_history():

    if not os.path.exists(FILE):
        return []

    try:

        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:

        return []



def save_history(history):

    with open(FILE, "w", encoding="utf-8") as f:

        json.dump(
            history,
            f,
            ensure_ascii=False,
            indent=4
        )



def add_message(question, answer):

    history = load_history()


    item = {
        "question": question,
        "answer": answer,
        "time": str(datetime.now())
    }


    history.append(item)


    save_history(history)


    return True



def show_history(limit=10):

    history = load_history()


    if not history:
        return "تاریخچه‌ای ندارم."


    result = "آخرین مکالمات:\n"


    for item in history[-limit:]:

        result += "\nسؤال: " + item["question"]
        result += "\nجواب: " + item["answer"] + "\n"


    return result
