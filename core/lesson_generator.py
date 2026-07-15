from core.lesson_reasoner import create_lesson
from core.lesson_memory import save_lesson



def generate_lesson(
    stage,
    topic,
    project
):

    result = create_lesson(
        stage
    )


    if not result:

        return None



    lesson = result.get(
        "lesson"
    )


    if not lesson:

        return None



    saved = save_lesson(
        topic,
        stage,
        lesson,
        project
    )


    print(
        "[LESSON GENERATOR] درس جدید ساخته و ذخیره شد 🧠"
    )


    return saved
