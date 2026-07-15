import json
import os


FILE = "data/agent_context.json"


def load_context():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def save_context(data):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def update_context(data):

    context = load_context()

    context.update(data)

    save_context(context)

    print("[AGENT CONTEXT] بروزرسانی شد 🧠")



def get_context():

    return load_context()
