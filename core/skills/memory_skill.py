from core.memory_parser import parse_memory
from core.personal_memory import remember, get_all_memory


NAME = "Memory"
VERSION = "1.0"
DESCRIPTION = "مدیریت حافظه کاربر"



def score(text):

    score = 0

    words = [
        "اسم",
        "سن",
        "من کی هستم",
        "درباره من"
    ]

    for word in words:

        if word in text:
            score += 20


    return score



def can_handle(text):

    memory = parse_memory(text)

    if memory:
        return True

    words = [
        "من کی هستم",
        "درباره من",
        "اطلاعات من",
        "مشخصات من",
        "اسم من",
        "سن من",
        "شهر من"
    ]

    for word in words:
        if word in text:
            return True

    return False



def run(text):

    memory = parse_memory(text)


    # ذخیره اطلاعات جدید
    if memory:

        answer = remember(
            memory["key"],
            memory["value"]
        )

        return answer



    # نمایش اطلاعات کاربر
    data = get_all_memory()


    if data:

        result = []

        for key, value in data.items():

            if isinstance(value, list):

                value = "، ".join(value)


            result.append(
                f"{key}: {value}"
            )


        return "\n".join(result)


    return "اطلاعاتی از شما ندارم"
