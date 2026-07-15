from core.experience_memory import save_experience
from core.experience_parser import parse_experience
from core.goal_engine import get_goal



def learn_experience(text):

    goal = get_goal()


    if not goal:

        return None



    topic = goal.get(
        "topic",
        "عمومی"
    )


    project = goal.get(
        "title",
        "پروژه ناشناس"
    )



    steps = goal.get(
        "steps",
        []
    )


    current = goal.get(
        "current_step",
        0
    )



    if current >= len(steps):

        return None



    stage = steps[current]



    # تشخیص جمله‌های تجربی

    markers = [
        "مشکل از",
        "فهمیدم",
        "تجربه کردم",
        "بهتره",
        "دفعه بعد",
        "یاد گرفتم",
        "متوجه شدم"
    ]



    is_experience = False


    for word in markers:

        if word in text:

            is_experience = True
            break



    if not is_experience:

        return None



    # تحلیل تجربه

    parsed = parse_experience(text)


    problem = parsed.get(
        "problem",
        text
    )


    solution = parsed.get(
        "solution",
        text
    )



    # ذخیره تجربه ساختاریافته

    result = save_experience(
        project,
        topic,
        stage,
        problem,
        solution
    )



    print(
        "[EXPERIENCE LEARNER] تجربه جدید یاد گرفته شد 🧠"
    )


    return result
