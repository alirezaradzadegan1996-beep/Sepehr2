from core.skill_engine import execute
from core.goal import Goal


def run(text):

    text = text.strip()

    # ساخت Goal
    goal = Goal(text)

    # ثبت اولین لاگ
    goal.add_log("Goal created")

    # اجرای مأموریت
    answer = execute(goal.text)

    if answer:

        goal.finish(answer)

        goal.add_log("Goal completed")

        return answer

    goal.status = "failed"

    goal.add_log("Goal failed")

    return None
