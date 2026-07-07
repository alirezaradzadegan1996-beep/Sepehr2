import json
import os

from core.learning_queue import remove_question


FILE = "data/knowledge.json"



def teach(text):

    if not text.startswith("یاد بگیر"):
        return None


    text = text.replace("یاد بگیر", "").strip()


    question = ""
    answer = ""


    # حالت سوال : جواب
    if ":" in text:

        question, answer = text.split(":", 1)


    # حالت جمله طبیعی
    elif " است" in text:

        parts = text.rsplit(" است", 1)

        question = parts[0].strip()
        answer = parts[1].strip()


        if answer:

            answer = answer + " است"



    else:

        return None



    question = question.strip()
    answer = answer.strip()


    if not question or not answer:
        return None



    if os.path.exists(FILE):

        with open(FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

    else:

        data = {}



    data[question] = answer



    with open(FILE, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


    remove_question(question)


    return "یاد گرفتم ✅"
