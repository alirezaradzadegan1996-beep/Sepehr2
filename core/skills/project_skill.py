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

    # نمایش وضعیت پروژه
    if "وضعیت" in text:
        return show_project()


    # ادامه پروژه
    if (
        "بعدی" in text
        or "ادامه" in text
        or "مرحله بعد" in text
    ):

        result = _pm.continue_project()

        if isinstance(result, dict):
            return result.get(
                "message",
                str(result)
            )

        return result


    # پایان پروژه
    if (
        "تمام کن" in text
        or "پایان پروژه" in text
    ):
        return finish_project()


    # شروع پروژه
    result = start_project(text)

    if isinstance(result, dict):
        return result.get(
            "message",
            str(result)
        )

    return result
