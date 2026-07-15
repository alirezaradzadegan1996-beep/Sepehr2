import json
import os


FILE = "data/learning_score.json"


def load_scores():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def save_scores(data):

    with open(FILE, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def add_score(question, answer, feedback):

    data = load_scores()


    found = None

    for item in data:

        if item["question"] == question and item["answer"] == answer:
            found = item
            break


    if found:

        if feedback == "good":
            found["score"] += 1

        elif feedback == "bad":
            found["score"] -= 1


        found["uses"] += 1


    else:

        score = 1 if feedback == "good" else -1

        data.append(
            {
                "question": question,
                "answer": answer,
                "score": score,
                "uses": 1
            }
        )


    save_scores(data)

    return "امتیاز یادگیری ثبت شد 🧠"



def get_scores():

    return load_scores()
