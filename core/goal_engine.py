import json
import os


FILE = "data/goals.json"


def load_goal():

    if not os.path.exists(FILE):
        return None

    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)


def save_goal(goal):

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            goal,
            f,
            ensure_ascii=False,
            indent=4
        )


def create_goal(title, topic, steps):

    goal = {
        "title": title,
        "topic": topic,
        "current_step": 0,
        "steps": steps
    }

    save_goal(goal)

    print("[GOAL] هدف جدید ثبت شد")

    return goal


def get_current_step():

    goal = load_goal()

    if not goal:
        return None

    return goal["steps"][goal["current_step"]]


def next_step():

    goal = load_goal()

    if not goal:
        return None

    if goal["current_step"] + 1 >= len(goal["steps"]):
        return "پروژه به پایان رسید ✅"

    goal["current_step"] += 1

    save_goal(goal)

    return goal["steps"][goal["current_step"]]


def has_goal():

    goal = load_goal()

    return goal is not None


def get_goal():

    return load_goal()


def reset_goal():

    if os.path.exists(FILE):
        os.remove(FILE)

    print("[GOAL] هدف حذف شد")


def project_status():

    goal = load_goal()

    if not goal:
        return "هیچ پروژه فعالی وجود ندارد."

    total = len(goal["steps"])

    current = goal["current_step"]

    return {
        "title": goal["title"],
        "current_step": current + 1,
        "total_steps": total,
        "current_task": goal["steps"][current]
    }
