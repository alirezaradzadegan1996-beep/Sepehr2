from core.project_learner import learn_project
from core.lesson_memory import save_lesson


def learn_lesson(project, topic):

    result = learn_project(
        project
    )


    if not result:

        return None



    best = result.get(
        "best_decision"
    )


    if not best:

        return None



    lesson = (
        f"در مرحله {best.get('stage')} "
        f"مشکل '{best.get('problem')}' "
        f"با تصمیم '{best.get('decision')}' "
        f"حل شد."
    )


    saved = save_lesson(
        topic,
        lesson,
        project
    )


    print(
        "[LESSON LEARNER] درس جدید یاد گرفته شد 🧠"
    )


    return saved
