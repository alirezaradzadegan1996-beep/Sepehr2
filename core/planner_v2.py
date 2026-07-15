import uuid
from datetime import datetime


def make_plan(task):

    task = task.strip()

    return {
        "id": str(uuid.uuid4())[:8],
        "goal": task,
        "status": "active",
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "step": 0,
        "steps": [
            "تحلیل درخواست",
            "طراحی راه‌حل",
            "ساخت فایل‌ها",
            "نوشتن کد",
            "تست",
            "رفع خطاها",
            "تحویل پروژه"
        ]
    }


def current_step(plan):

    if plan["step"] >= len(plan["steps"]):
        return None

    return plan["steps"][plan["step"]]



def next_step(plan):

    if plan["step"] >= len(plan["steps"]) - 1:
        plan["status"] = "completed"
        plan["updated_at"] = datetime.now().isoformat(timespec="seconds")
        return None


    plan["step"] += 1

    plan["updated_at"] = datetime.now().isoformat(timespec="seconds")

    return plan["steps"][plan["step"]]
