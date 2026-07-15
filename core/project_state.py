import json
import os

FILE = "data/project_state.json"


def save_project(plan):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(plan, f, ensure_ascii=False, indent=4)


def load_project():
    if not os.path.exists(FILE):
        return None

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def clear_project():
    if os.path.exists(FILE):
        os.remove(FILE)
