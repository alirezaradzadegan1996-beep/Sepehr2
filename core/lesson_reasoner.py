from core.decision_memory import find_decision


def create_lesson(stage):

    decision = find_decision(stage)


    if not decision:

        return None



    problem = decision.get(
        "problem",
        ""
    )

    action = decision.get(
        "decision",
        ""
    )

    result = decision.get(
        "result",
        ""
    )


    lesson = (
        f"در مرحله {stage}، "
        f"وقتی مشکل «{problem}» رخ داد، "
        f"تصمیم «{action}» باعث شد "
        f"نتیجه «{result}» به دست بیاید."
    )


    return {
        "source": "lesson_reasoner",
        "lesson": lesson,
        "rank": 12
    }
