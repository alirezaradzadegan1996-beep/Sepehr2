from core.conversation_memory import add_message
from core.feedback_handler import handle_feedback, set_last_question


def chat_response(text):

    text = text.strip()


    # =========================
    # Feedback
    # =========================

    feedback = handle_feedback(text)

    if feedback:
        return feedback



    # =========================
    # Simple Conversation
    # =========================

    responses = {

        "خوبی؟": "ممنون علیرضا، خوبم 😊 آماده‌ام کمک کنم.",

        "خوبی": "ممنون علیرضا، خوبم 😊 آماده‌ام.",

        "چه خبر؟": "همه چیز آماده است. دارم روی یادگیری و بهتر شدن کار می‌کنم.",

        "اسمت چیه؟": "من سپهر هستم 🤖",

        "کی هستی؟": "من سپهر هستم، دستیار هوشمند شخصی تو."
    }


    if text in responses:

        answer = responses[text]

        add_message(
            text,
            answer
        )

        return answer



    # =========================
    # Unknown Chat
    # =========================

    set_last_question(text)

    answer = "دارم یاد می‌گیرم بهتر جواب بدم. 😊"


    add_message(
        text,
        answer
    )


    return answer
