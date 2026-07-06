import json
import os


FILE = "data/unknown.json"



def load_unknown():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def save_unknown(items):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            items,
            f,
            ensure_ascii=False,
            indent=4
        )



def add_unknown(question):

    items = load_unknown()

    if question not in items:

        items.append(question)

        save_unknown(items)

        return True

    return False
