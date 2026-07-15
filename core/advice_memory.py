import json
import os


FILE = "data/advice_memory.json"



def load_advice():

    if not os.path.exists(FILE):

        return []


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_advice(
    topic,
    stage,
    advice
):

    data = load_advice()


    item = {
        "topic": topic,
        "stage": stage,
        "advice": advice,
        "uses": 1
    }


    data.append(item)


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


    print("[ADVICE MEMORY] ذخیره شد 🧠")

    return item



def find_advice(stage):

    data = load_advice()


    results = []


    for item in data:

        if item.get("stage") == stage:

            results.append(item)



    if not results:

        return None



    results.sort(
        key=lambda x: x.get("uses", 0),
        reverse=True
    )


    best = results[0]


    print("[ADVICE MEMORY] تجربه پیدا شد")

    return best["advice"]
