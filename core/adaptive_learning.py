import json
import os


FILE = "data/learning_score.json"



def load_data():

    if not os.path.exists(FILE):
        return []


    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)




def save_data(data):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )




def reward_answer(question, answer):

    data = load_data()


    for item in data:

        if (
            item["question"] == question
            and item["answer"] == answer
        ):

            item["score"] = item.get("score", 0) + 1

            item["uses"] = item.get("uses", 0) + 1

            save_data(data)

            print("[ADAPTIVE] جواب تقویت شد 🧠")

            return item



    # اگر تجربه جدید بود

    new_item = {
        "question": question,
        "answer": answer,
        "score": 1,
        "uses": 1
    }


    data.append(new_item)

    save_data(data)


    print("[ADAPTIVE] تجربه جدید ذخیره شد 🧠")

    return new_item




def punish_answer(question, answer):

    data = load_data()


    for item in data:

        if (
            item["question"] == question
            and item["answer"] == answer
        ):

            item["score"] = max(
                0,
                item.get("score", 0) - 1
            )

            save_data(data)


            print("[ADAPTIVE] جواب ضعیف شد ⚠️")

            return item


    return None
