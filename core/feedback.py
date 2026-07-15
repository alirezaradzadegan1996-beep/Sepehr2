import json
import os


FILE = "data/knowledge.json"


def update_feedback(question, positive=True):

    if not os.path.exists(FILE):
        return False


    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)


    item = data.get(question)


    if not isinstance(item, dict):
        return False


    confidence = item.get("confidence", 1)


    if positive:

        confidence += 1

        if confidence > 10:
            confidence = 10

    else:

        confidence -= 1

        if confidence < 0:
            confidence = 0


    item["confidence"] = confidence


    data[question] = item


    with open(FILE, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


    return True
