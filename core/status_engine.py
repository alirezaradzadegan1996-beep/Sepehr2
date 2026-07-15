from core.goal_engine import get_goal


def get_status():

    goal = get_goal()

    if not goal:
        return "پروژه فعالی وجود ندارد."


    steps = goal.get("steps", [])
    current = goal.get("current_step", 0)


    if current >= len(steps):
        return (
            f"پروژه {goal.get('title')} "
            "به پایان رسیده است."
        )


    current_task = steps[current]


    return (
        f"📌 پروژه: {goal.get('title')}\n"
        f"موضوع: {goal.get('topic')}\n"
        f"مرحله فعلی: {current + 1}/{len(steps)}\n"
        f"کار فعلی: {current_task}"
    )
