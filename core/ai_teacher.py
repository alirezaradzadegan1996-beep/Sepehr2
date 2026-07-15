from core.ai_learning import learn_from_ai


def should_learn(question, answer):

    ignore_words = [
        "سلام",
        "خداحافظ",
        "مرسی",
        "ممنون"
    ]

    for word in ignore_words:
        if word in question:
            return False


    bad_answers = [
        "خطا در اتصال",
        "کلید هوش مصنوعی تنظیم نشده",
        "error",
        "خطای AI"
    ]

    for item in bad_answers:
        if item in answer:
            return False


    if len(answer) < 10:
        return False


    return True



def teach_from_ai(question, answer):

    if not should_learn(question, answer):
        return False

    result = learn_from_ai(
        question,
        answer
    )

    return result
