import json
import os


FILE = "data/knowledge.json"

MAX_CONFIDENCE = 10



def increase_confidence(question):

    if not os.path.exists(FILE):
        return False


    with open(FILE, "r", encoding="utf-8") as f:
        data = json.load(f)


    item = data.get(question)


    if isinstance(item, dict):

        confidence = item.get("confidence", 1)


        if confidence < MAX_CONFIDENCE:

            item["confidence"] = confidence + 1


        data[question] = item


        with open(FILE, "w", encoding="utf-8") as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )


        return True


    return False



def get_confidence_level(value):

    if value <= 3:

        return "ضعیف"


    elif value <= 7:

        return "قابل اعتماد"


    else:

        return "تثبیت شده"
