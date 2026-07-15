import json
import os
from datetime import datetime


FILE = "data/agent_memory.json"


def load_memory():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def save_memory(data):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def remember_action(action, message):

    data = load_memory()

    data["last_action"] = action.get("action")
    data["last_message"] = message
    data["time"] = str(datetime.now())

    save_memory(data)

    print("[AGENT MEMORY] ذخیره شد 🧠")



def get_agent_memory():

    return load_memory()
