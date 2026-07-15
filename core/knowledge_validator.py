def validate(answer):

    if not answer:
        return False


    # جواب خیلی کوتاه نباشد
    if len(answer.strip()) < 5:
        return False


    # خطاهای رایج AI ذخیره نشوند
    bad_words = [
        "کلید هوش مصنوعی تنظیم نشده",
        "خطا در اتصال AI",
        "خطای AI",
        "نامشخص"
    ]


    for word in bad_words:

        if word in answer:
            return False


    return True
