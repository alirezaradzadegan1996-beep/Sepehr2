from core.intent import detect_intent
from core.memory_parser import parse_memory
from core.personal_memory import (
    remember,
    recall,
    memory_summary,
    forget
)
from core.feedback_handler import (
    handle_feedback,
    set_last_question
)
from core.ai_router import route
from core.conversation_memory import add_message, show_history


def process(text):

    text = text.strip()


    # ---------- Feedback ----------
    feedback = handle_feedback(text)

    if feedback:
        return feedback


    # ---------- Personal Memory ----------
    memory = parse_memory(text)

    if memory:

        return remember(
            memory["key"],
            memory["value"]
        )


    # ---------- Intent ----------
    intent = detect_intent(text)


    if intent == "memory":

        if "آخرین" in text or "تاریخچه" in text:

            return show_history()


        if "من کی هستم" in text:

            return memory_summary()


        if "فراموش کن" in text:

            if "اسم" in text:
                return forget("name")

            if "شهر" in text:
                return forget("city")

            if "سن" in text:
                return forget("age")

            if "شغل" in text:
                return forget("job")

            if "هدف" in text:
                return forget("goals")

            if "علاقه" in text:
                return forget("interests")


    # ---------- AI ----------
    set_last_question(text)

    answer = route(text)

    add_message(
        text,
        answer
    )

    return answer
