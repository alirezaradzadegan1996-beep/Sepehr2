from core.reasoning_engine import reason
from core.learning_manager import get_learned_answer, learn_answer
from core.local_ai import generate_answer
from core.response_memory import save_last_response
from core.answer_evaluator import evaluate_answer
from core.topic_classifier import detect_topic

from core.planning_engine import create_plan
from core.goal_engine import create_goal
from core.goal_engine import next_step
from core.goal_engine import has_goal


def route(text):

    text = text.strip()

    # -----------------------------
    # ادامه پروژه
    # -----------------------------
    if text in [
        "بعدی",
        "ادامه",
        "ادامه بده",
        "مرحله بعد"
    ]:

        if has_goal():
            return next_step()

    # -----------------------------
    # شروع پروژه جدید
    # -----------------------------
    if (
        "میخواهم" in text
        or "می‌خواهم" in text
        or "پروژه" in text
    ):

        plan = create_plan(text)

        if plan:

            create_goal(
                text,
                plan["topic"],
                plan["steps"]
            )

            return (
                "✅ پروژه ثبت شد\n\n"
                "مرحله اول:\n"
                + plan["steps"][0]
            )

    # -----------------------------
    # موتور استدلال
    # -----------------------------
    result = reason(text)

    if result:

        answer = result["answer"]

        save_last_response(
            text,
            answer
        )

        return answer

    # -----------------------------
    # حافظه یادگیری
    # -----------------------------
    learned = get_learned_answer(text)

    if learned:

        save_last_response(
            text,
            learned
        )

        return learned

    # -----------------------------
    # Local AI
    # -----------------------------
    print("[LOCAL AI] تولید پاسخ")

    topic = detect_topic(text)

    print("[TOPIC]", topic)

    answer = generate_answer(
        text,
        topic
    )

    # -----------------------------
    # ارزیابی پاسخ
    # -----------------------------
    evaluation = evaluate_answer(
        text,
        answer
    )

    if evaluation["quality"] == "good":

        print("[LEARNING] جواب تایید شد ✅")

        learn_answer(
            text,
            answer
        )

    else:

        print("[LEARNING] جواب ضعیف بود، ذخیره نشد ⚠️")

    # -----------------------------
    # ذخیره آخرین پاسخ
    # -----------------------------
    save_last_response(
        text,
        answer
    )

    return answer
