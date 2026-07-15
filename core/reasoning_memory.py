from core.goal_engine import get_goal
from core.decision_memory import find_decision
from core.lesson_memory import find_lesson



def find_project_reason():

    goal = get_goal()


    if not goal:

        return None



    topic = goal.get(
        "topic",
        ""
    )


    # ---------- Lesson Memory ----------

    lesson = find_lesson(topic)


    if lesson:

        return {
            "source": "lesson_memory",
            "answer":
                f"📚 درس قبلی سپهر:\n"
                f"{lesson.get('lesson')}\n"
                f"📂 منبع: {lesson.get('source')}",
            "rank": lesson.get(
                "score",
                13
            )
        }



    # ---------- Decision Memory ----------

    steps = goal.get(
        "steps",
        []
    )


    for stage in steps:

        decision = find_decision(stage)


        if decision:

            return {
                "source": "decision_memory",
                "answer":
                    f"🧠 تجربه تصمیم قبلی سپهر:\n"
                    f"مرحله: {stage}\n"
                    f"مشکل: {decision.get('problem')}\n"
                    f"تصمیم: {decision.get('decision')}\n"
                    f"نتیجه: {decision.get('result')}",
                "rank": decision.get(
                    "score",
                    10
                )
            }



    return None
