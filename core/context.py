import json
import os


CONTEXT_FILE = "data/context.json"


def load_context():

    if not os.path.exists(CONTEXT_FILE):
        return {
            "topic": None,
            "history": []
        }

    with open(CONTEXT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)



def save_context(context):

    with open(CONTEXT_FILE, "w", encoding="utf-8") as f:
        json.dump(
            context,
            f,
            ensure_ascii=False,
            indent=4
        )



def update_topic(topic):

    context = load_context()

    if topic:
        context["topic"] = topic

    save_context(context)

    return context["topic"]



def get_topic():

    return load_context().get("topic")



def add_history(text):

    context = load_context()

    history = context.get("history", [])

    if not history or history[-1] != text:

        history.append(text)


    if len(history) > 10:
        history = history[-10:]


    context["history"] = history

    save_context(context)



def get_history():

    return load_context().get("history", [])



def set_topic(topic):

    return update_topic(topic)
