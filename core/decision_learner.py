from core.goal_engine import get_goal
from core.decision_parser import parse_decision
from core.decision_memory import save_decision
from core.lesson_generator import generate_lesson



def learn_decision(text):

    goal = get_goal()


    if not goal:

        return None



    data = parse_decision(text)


    if not data:

        return None



    stage = goal.get(
        "steps",
        []
    )[goal.get(
        "current_step",
        0
    )]



    result = save_decision(
        goal.get(
            "title",
            "پروژه"
        ),
        stage,
        data.get(
            "problem"
        ),
        data.get(
            "decision"
        ),
        data.get(
            "result"
        )
    )



    print(
        "[DECISION LEARNER] تصمیم جدید یاد گرفته شد 🧠"
    )



    # ساخت خودکار درس از تصمیم

    generate_lesson(
        stage,
        goal.get(
            "topic",
            "عمومی"
        ),
        goal.get(
            "title",
            "پروژه"
        )
    )



    return result
