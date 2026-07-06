import json
import os


FILE = "data/knowledge.json"



def load_knowledge():

    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def show_knowledge():

    data = load_knowledge()

    if not data:
        return "هنوز چیزی یاد نگرفتم."

    result = "چیزهایی که یاد گرفتم:\n"

    for key in data:

        result += f"- {key}\n"

    return result



def forget_knowledge(word):

    data = load_knowledge()

    removed = False


    for key in list(data.keys()):

        if word in key:

            del data[key]
            removed = True


    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


    if removed:
        return "فراموش کردم ✅"

    return "این مورد را پیدا نکردم."
