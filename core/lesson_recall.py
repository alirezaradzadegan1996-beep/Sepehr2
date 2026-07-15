from core.lesson_memory import find_lesson


def recall_lesson(topic):

    lesson = find_lesson(
        topic
    )


    if not lesson:

        return None



    print(
        "[LESSON RECALL] درس مرتبط پیدا شد 🧠"
    )


    return (
        f"🧠 درس قبلی سپهر:\n"
        f"{lesson.get('lesson')}\n"
        f"📂 منبع: {lesson.get('source')}"
    )
