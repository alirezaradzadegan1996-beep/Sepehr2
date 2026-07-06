from core.context import get_topic, get_history


FOLLOW_WORDS = [
    "اولیش",
    "دومیش",
    "بعدی",
    "همون",
    "همونی",
    "ادامه بده",
    "توضیح بده",
    "بیشتر بگو",
    "ادامه"
]

def resolve_context(text):

    text = text.strip()

    for word in FOLLOW_WORDS:

        if word in text:

            return {
                "resolved": True,
                "topic": get_topic(),
                "history": get_history()
            }

    return None
