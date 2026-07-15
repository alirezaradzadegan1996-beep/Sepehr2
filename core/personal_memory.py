import json
import os


FILE = "data/personal_memory.json"



def load_memory():

    if not os.path.exists(FILE):
        return {}

    try:

        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:

        return {}



def save_memory(data):

    with open(FILE, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def remember(key, value):

    data = load_memory()

    data[key] = value

    save_memory(data)

    return "یاد گرفتم ✅"



def recall(key):

    data = load_memory()

    return data.get(key)



def forget(key):

    data = load_memory()

    if key in data:

        del data[key]

        save_memory(data)

        return "فراموش کردم ✅"


    return "چیزی برای فراموش کردن پیدا نکردم."



def get_all_memory():

    return load_memory()



def memory_summary():

    data = load_memory()


    if not data:

        return "هنوز چیزی از شما یاد نگرفتم."


    labels = {

        "name": "اسم",
        "age": "سن",
        "city": "شهر",
        "job": "شغل",
        "favorite_color": "رنگ مورد علاقه",
        "interests": "علاقه‌ها",
        "goals": "هدف‌ها"

    }


    result = []


    for key, value in data.items():

        title = labels.get(key, key)

        if isinstance(value, list):

            value = "، ".join(value)


        result.append(
            f"{title}: {value}"
        )


    return "\n".join(result)
