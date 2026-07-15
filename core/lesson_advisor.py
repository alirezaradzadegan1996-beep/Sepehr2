from core.lesson_memory import find_lesson



def advise_from_lesson(
    topic,
    stage
):

    lesson = find_lesson(
        topic,
        stage
    )


    if not lesson:

        return None



    text = lesson.get(
        "lesson",
        ""
    )


    return {
        "source": "lesson_advisor",

        "advice":
            f"💡 پیشنهاد سپهر:\n"
            f"{text}\n\n"
            f"📌 مرحله مرتبط: "
            f"{lesson.get('stage')}\n"
            f"📂 بر اساس تجربه پروژه: "
            f"{lesson.get('source')}",

        "rank": lesson.get(
            "score",
            lesson.get(
                "uses",
                0
            )
        )
    }
