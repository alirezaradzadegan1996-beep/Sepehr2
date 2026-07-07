import json
import os


FILE = "data/learning_queue.json"


def load_queue():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def save_queue(queue):

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(
            queue,
            f,
            ensure_ascii=False,
            indent=4
        )



def add_question(text):

    queue = load_queue()

    if text not in queue:

        queue.append(text)

        save_queue(queue)

        return True

    return False



def remove_question(text):

    queue = load_queue()

    if text in queue:

        queue.remove(text)

        save_queue(queue)

        return True

    return False



def show_queue():

    queue = load_queue()


    if not queue:
        return "چیزی در صف یادگیری نیست."


    result = "منتظر یادگیری:\n"


    for item in queue:

        result += f"- {item}\n"


    return result
