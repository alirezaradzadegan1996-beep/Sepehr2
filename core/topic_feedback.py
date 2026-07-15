import json
import os


FILE = "data/topic_memory.json"



def load_topics():

    if not os.path.exists(FILE):

        return []


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)




def save_topics(data):

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




def reward_topic_answer(
    answer
):

    data = load_topics()


    changed = False


    for item in data:

        if item.get("answer") == answer:

            item["score"] = item.get(
                "score",
                0
            ) + 1


            item["uses"] = item.get(
                "uses",
                0
            ) + 1


            item["confidence"] = item.get(
                "confidence",
                1
            ) + 1


            changed = True



    if changed:

        save_topics(data)


        print(
            "[TOPIC FEEDBACK] تجربه تقویت شد 🧠"
        )


        return True



    return False




def punish_topic_answer(
    answer
):

    data = load_topics()


    changed = False


    for item in data:

        if item.get("answer") == answer:

            item["score"] = item.get(
                "score",
                0
            ) - 1


            changed = True



    if changed:

        save_topics(data)


        print(
            "[TOPIC FEEDBACK] تجربه ضعیف شد ⚠️"
        )


        return True



    return False
