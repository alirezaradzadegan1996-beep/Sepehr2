from core.status_engine import get_status
from core.goal_engine import next_step, create_goal
from core.task_engine import complete_current_step
from core.reasoning_engine import reason
from core.planning_engine import create_plan
from core.local_ai import generate_answer
from core.topic_classifier import detect_topic
from core.advisor_engine import advise
from core.experience_learner import learn_experience
from core.decision_learner import learn_decision


def execute(action, text):

    name = action["action"]

    print("[EXECUTOR]", name)



    # --------------------------
    # شروع پروژه
    # --------------------------
    if name == "start_project":

        plan = create_plan(text)


        if not plan:

            return "خطا در ساخت پروژه"



        create_goal(
            text,
            plan["topic"],
            plan["steps"]
        )


        response = (
            "✅ پروژه ثبت شد\n\n"
        )


        if plan.get("previous_lesson"):

            response += (
                plan["previous_lesson"]
                + "\n\n"
            )


        response += (
            "📋 مرحله اول:\n"
            + plan["steps"][0]
        )


        return response



    # --------------------------
    # مرحله بعد
    # --------------------------
    if name == "next_step":

        return next_step()



    # --------------------------
    # اتمام مرحله
    # --------------------------
    if name == "complete_step":

        return complete_current_step()



    # --------------------------
    # وضعیت پروژه
    # --------------------------
    if name == "project_status":

        return get_status()



    # --------------------------
    # پیشنهاد پروژه
    # --------------------------
    if name == "project_advice":

        return advise()



    # --------------------------
    # یادگیری تجربه
    # --------------------------
    if name == "learn_experience":

        result = learn_experience(text)


        if result:

            return "🧠 تجربه جدید سپهر ثبت شد."


        return "تجربه‌ای برای یادگیری پیدا نشد."



    # --------------------------
    # یادگیری تصمیم
    # --------------------------
    if name == "learn_decision":

        result = learn_decision(text)


        if result:

            return "🧠 تصمیم جدید سپهر ثبت شد."


        return "تصمیمی برای یادگیری پیدا نشد."



    # --------------------------
    # موتور استدلال
    # --------------------------
    if name == "reason":

        return action["result"]["answer"]



    # --------------------------
    # Local AI
    # --------------------------
    if name == "local_ai":

        topic = detect_topic(text)


        return generate_answer(
            text,
            topic
        )



    return "عمل ناشناخته"
