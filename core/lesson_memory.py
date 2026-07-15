import json
import os

from core.lesson_scorer import rank_lessons


FILE = "data/lesson_memory.json"



def load_lessons():

    if not os.path.exists(FILE):

        return []


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_lessons(data):

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def save_lesson(
    topic,
    stage,
    lesson,
    source
):

    data = load_lessons()


    item = {
        "topic": topic,
        "stage": stage,
        "lesson": lesson,
        "source": source,
        "uses": 1
    }


    data.append(item)


    save_lessons(data)


    print(
        "[LESSON MEMORY] درس ذخیره شد 🧠"
    )


    return item



def find_lesson(
    topic,
    stage=None
):

    data = load_lessons()


    results = []


    for item in data:

        if item.get("topic") == topic:


            if stage and item.get("stage") != stage:

                continue


            item["uses"] = item.get(
                "uses",
                1
            ) + 1


            results.append(item)



    if not results:

        return None



    ranked = rank_lessons(
        results
    )


    best = ranked[0]


    print(
        "[LESSON MEMORY] بهترین درس انتخاب شد 🧠"
    )


    return best
