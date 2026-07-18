from core.intent import detect_intent
from core.memory_parser import parse_memory

from core.cortex.cortex import cortex
from core.cortex.bootstrap import boot

from core.feedback_handler import (
    handle_feedback,
    set_last_question,
)

from core.ai_router import route

from core.conversation_memory import (
    add_message,
    show_history,
)


def process(text):

    text = text.strip()

    # ---------- Cortex Auto Boot ----------

    if not cortex.has("memory"):
        boot()


    # ---------- Feedback ----------

    feedback = handle_feedback(text)

    if feedback:
        return feedback


    # ---------- Personal Memory ----------

    memory_service = cortex.get("memory")

    memory = parse_memory(text)

    if memory:

        return memory_service.remember(
            memory["key"],
            memory["value"],
        )


    # ---------- Intent ----------

    intent = detect_intent(text)


    if intent == "memory":

        if "آخرین" in text or "تاریخچه" in text:
            return show_history()


        if "من کی هستم" in text:

            return memory_service.summary()


        if "فراموش کن" in text:

            if "اسم" in text:
                return memory_service.forget("name")

            if "شهر" in text:
                return memory_service.forget("city")

            if "سن" in text:
                return memory_service.forget("age")

            if "شغل" in text:
                return memory_service.forget("job")

            if "هدف" in text:
                return memory_service.forget("goals")

            if "علاقه" in text:
                return memory_service.forget("interests")


    # ---------- AI ----------

    set_last_question(text)


    answer = route(text)

    # ---------- Cortex Context ----------
    context_service = cortex.get("context")

    if context_service:
        context_service.update(
            text,
            answer
        )

    # ---------- Conversation Memory ----------
    add_message(
        text,
        answer,
    )

    return answer
