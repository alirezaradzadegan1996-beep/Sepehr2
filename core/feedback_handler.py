import json
import os

from core.feedback import update_feedback


SESSION_FILE = "data/session.json"



def save_last_question(question):

    data = {
        "last_question": question
    }


    with open(SESSION_FILE, "w", encoding="utf-8") as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )



def load_last_question():

    if not os.path.exists(SESSION_FILE):

        return None


    try:

        with open(SESSION_FILE, "r", encoding="utf-8") as f:

            data = json.load(f)

            return data.get("last_question")


    except Exception:

        return None



def set_last_question(question):

    save_last_question(question)



def handle_feedback(text):

    last_question = load_last_question()


    if not last_question:

        return None



    positive_words = [
        "درسته",
        "درست است",
        "صحیحه",
        "آفرین",
        "خوبه"
    ]


    negative_words = [
        "اشتباهه",
        "غلطه",
        "درست نیست",
        "اشتباه است"
    ]



    for word in positive_words:

        if word in text:

            update_feedback(
                last_question,
                True
            )

            return "خوشحالم که درست بود ✅"



    for word in negative_words:

        if word in text:

            update_feedback(
                last_question,
                False
            )

            return "متوجه شدم، اعتماد این پاسخ را کم کردم ⚠️"



    return None
