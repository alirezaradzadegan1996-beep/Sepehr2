from core.ai_learning import save_ai_answer, find_ai_answer


def get_learned_answer(text):
    """
    بررسی می‌کند آیا جواب قبلاً یاد گرفته شده یا نه
    """

    answer = find_ai_answer(text)

    if answer:
        print("[LEARNING MEMORY] جواب پیدا شد")
        return answer

    return None



def learn_answer(question, answer):
    """
    ذخیره جواب جدید در حافظه یادگیری
    """

    if not answer:
        return None


    result = save_ai_answer(
        question,
        answer
    )


    if result:
        print("[LEARNING MANAGER] ذخیره شد")


    return result
