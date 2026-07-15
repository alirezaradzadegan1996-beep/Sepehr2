from core.ai_connector import ask_ai
from core.project_manager import start_project, continue_project
from core.memory_parser import parse_memory
from core.personal_memory import remember, get_all_memory
from core.conversation_memory import show_history
from core.feedback_handler import handle_feedback, set_last_question
from core.feedback_router import process_feedback
from core.ai_router import route
from core.intent import detect_intent


def think(text):

    text = text.strip()


    # بازخورد یادگیری جدید
    feedback = process_feedback(text)

    if feedback:
        return feedback


    # بازخورد قدیمی سیستم
    feedback = handle_feedback(text)

    if feedback:
        return feedback


    # پروژه جدید
    if "بساز" in text or "طراحی کن" in text:
        return start_project(text)


    # ادامه پروژه
    if text in ["بعدی", "ادامه", "ادامه بده"]:
        return continue_project()


    # حافظه شخصی
    memory = parse_memory(text)

    if memory:
        return remember(
            memory["key"],
            memory["value"]
        )


    # اطلاعات درباره کاربر
    if text == "من کی هستم":

        data = get_all_memory()

        if not data:
            return "هنوز چیزی درباره شما نمی‌دانم."


        lines = []

        names = {
            "name": "اسم",
            "city": "شهر",
            "job": "شغل",
            "age": "سن",
            "favorite_color": "رنگ مورد علاقه",
            "interests": "علاقه‌ها",
            "goals": "هدف‌ها"
        }


        for key, value in data.items():

            title = names.get(key, key)

            if isinstance(value, list):
                value = "، ".join(value)

            lines.append(
                f"{title}: {value}"
            )


        return "\n".join(lines)


    # تاریخچه
    if detect_intent(text) == "memory":

        if "آخرین" in text or "تاریخچه" in text:
            return show_history()


    # ذخیره سوال جدید
    set_last_question(text)


    # مسیر اصلی هوش سپهر
    answer = route(text)


    if answer:
        return answer


    # اتصال OpenAI (در آینده)
    ai_answer = ask_ai(text)


    if ai_answer:
        return ai_answer


    return "فعلاً پاسخی برای این سؤال ندارم."
