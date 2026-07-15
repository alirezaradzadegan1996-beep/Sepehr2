import json
import os


FILE = "data/ai_learning.json"


BAD_ANSWERS = [
    "فعلاً پاسخی برای این سؤال ندارم.",
    "نمی‌دانم",
    "اطلاعی ندارم",
    "اطلاعاتی ندارم",
    "جوابی ندارم"
]



def is_valid_answer(answer):

    if not answer:
        return False

    answer = answer.strip()

    for bad in BAD_ANSWERS:

        if bad in answer:
            return False

    return True




def load_ai_memory():

    if not os.path.exists(FILE):

        return []

    with open(FILE, "r", encoding="utf-8") as f:

        return json.load(f)




def save_ai_answer(question, answer):

    if not is_valid_answer(answer):

        print("[AI LEARNING] جواب معتبر نیست، ذخیره نشد")

        return "skip"



    memory = load_ai_memory()



    item = {

        "question": question,

        "answer": answer,

        "status": "learned"

    }



    memory.append(item)



    with open(FILE, "w", encoding="utf-8") as f:

        json.dump(

            memory,

            f,

            ensure_ascii=False,

            indent=4

        )



    return "جواب ذخیره شد 🧠"





def find_ai_answer(question):

    memory = load_ai_memory()


    for item in memory:

        if item["question"] == question:

            return item["answer"]


    return None





def clear_ai_answer():

    if os.path.exists(FILE):

        os.remove(FILE)
