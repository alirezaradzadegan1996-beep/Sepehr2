from core.goal_engine import has_goal
from core.goal_engine import next_step


def complete_current_step():

    if not has_goal():
        return "هیچ پروژه فعالی وجود ندارد."

    step = next_step()

    return (
        "✅ مرحله با موفقیت ثبت شد.\n\n"
        "مرحله بعد:\n"
        + step
    )
