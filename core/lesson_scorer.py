def score_lesson(lesson):

    score = 0


    text = lesson.get(
        "lesson",
        ""
    )


    # تعداد استفاده

    score += lesson.get(
        "uses",
        0
    )


    # درس کامل‌تر

    if len(text) > 50:

        score += 3


    if len(text) > 100:

        score += 5



    # داشتن اطلاعات مشکل

    if "مشکل" in text:

        score += 3



    # داشتن نتیجه

    if "نتیجه" in text:

        score += 3



    # منبع پروژه

    if lesson.get("source"):

        score += 2



    return score



def rank_lessons(lessons):

    ranked = []


    for lesson in lessons:

        item = lesson.copy()

        item["score"] = score_lesson(
            item
        )

        ranked.append(item)



    ranked.sort(
        key=lambda x: x.get(
            "score",
            0
        ),
        reverse=True
    )


    return ranked
