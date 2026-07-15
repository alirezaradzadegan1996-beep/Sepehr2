from core.goal_engine import get_goal
from core.lesson_advisor import advise_from_lesson
from core.advice_memory import find_advice
from core.decision_memory import find_decision
from core.decision_reasoner import explain_decision



def advise():

    goal = get_goal()


    if not goal:

        return "پروژه فعالی وجود ندارد."


    steps = goal.get(
        "steps",
        []
    )


    current = goal.get(
        "current_step",
        0
    )


    if current >= len(steps):

        return "✅ پروژه به پایان رسیده است."



    task = steps[current]


    topic = goal.get(
        "topic",
        ""
    )



    # --------------------------
    # Lesson Advisor
    # --------------------------

    lesson = advise_from_lesson(
        topic
    )


    if lesson:

        return (
            f"📌 مرحله فعلی: {task}\n\n"
            f"{lesson.get('advice')}"
        )



    # --------------------------
    # Decision Memory
    # --------------------------

    decision = find_decision(
        task
    )


    if decision:

        explanation = explain_decision(
            decision
        )


        return (
            f"📌 مرحله فعلی: {task}\n\n"
            f"🧠 تصمیم منتخب سپهر:\n"
            f"مشکل: {decision.get('problem')}\n"
            f"تصمیم: {decision.get('decision')}\n"
            f"نتیجه: {decision.get('result')}\n\n"
            f"📊 دلیل انتخاب:\n"
            f"{explanation}"
        )



    # --------------------------
    # Advice Memory
    # --------------------------

    memory_advice = find_advice(
        task
    )


    if memory_advice:

        return (
            f"📌 مرحله فعلی: {task}\n\n"
            f"🧠 تجربه قبلی سپهر:\n"
            f"{memory_advice}"
        )



    # --------------------------
    # Basic Advice
    # --------------------------

    advice_map = {

        "مشخص کردن هدف پهپاد":
            "ابتدا کاربرد دقیق پهپاد را مشخص کن.",

        "انتخاب نوع پهپاد":
            "بر اساس هدف، نوع پهپاد را انتخاب کن.",

        "انتخاب موتور و ملخ":
            "وزن، تراست و توان موتور را بررسی کن.",

        "انتخاب کنترلر پرواز":
            "کنترلر مناسب مثل Pixhawk انتخاب کن.",

        "انتخاب باتری":
            "ظرفیت، جریان‌دهی و وزن باتری را بررسی کن.",

        "طراحی بدنه":
            "فریم را با توجه به وزن قطعات طراحی کن.",

        "مونتاژ قطعات":
            "سیم‌کشی و اتصال قطعات را بررسی کن.",

        "برنامه نویسی":
            "تنظیمات کنترلر و سنسورها را انجام بده.",

        "تست پرواز":
            "قبل از پرواز، تست موتور و کالیبراسیون انجام بده."
    }



    advice = advice_map.get(
        task,
        "این مرحله را با دقت بررسی کن."
    )


    return (
        f"📌 مرحله فعلی: {task}\n"
        f"💡 پیشنهاد سپهر: {advice}"
    )
