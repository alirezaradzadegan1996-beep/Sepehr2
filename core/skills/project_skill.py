from core.project_manager import (
    start_project,
    show_project,
    finish_project,
    _pm
)

from core.skills.app_builder import AppBuilder


NAME = "Project"
VERSION = "1.0"
DESCRIPTION = "مدیریت و ساخت پروژه‌ها"


def score(text):

    score = 0

    words = [
        "پروژه",
        "بساز",
        "اپ",
        "بعدی",
        "وضعیت پروژه"
    ]

    for word in words:
        if word in text:
            score += 20

    return score



def can_handle(text):

    words = [
        "بساز",
        "ساخت",
        "پروژه",
        "اپ",
        "وضعیت پروژه",
        "بعدی",
        "ادامه",
        "تمام کن"
    ]

    for word in words:
        if word in text:
            return True

    return False



def run(text):

    # نمایش وضعیت
    if "وضعیت" in text:
        return show_project()


    # ادامه پروژه
    if (
        "بعدی" in text
        or "ادامه" in text
    ):

        project = _pm.get_active()

        if not project:
            return "❌ پروژه فعالی وجود ندارد."


        step_name = _pm.next_step()


        if step_name is None:
            return "✅ پروژه کامل شد."


        project = _pm.get_active()


        result = AppBuilder.run(
            project,
            project["step"]
        )


        return (
            f"📌 پروژه: {project['goal']}\n\n"
            f"مرحله {project['step'] + 1}:\n"
            f"{result['message']}"
        )


    # پایان پروژه
    if (
        "تمام کن" in text
        or "پایان پروژه" in text
    ):
        return finish_project()



    # شروع پروژه
    return start_project(text)
