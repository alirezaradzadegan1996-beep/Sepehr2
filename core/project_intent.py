def detect_project_intent(text):

    text = text.strip()


    # وضعیت پروژه
    status_words = [
        "وضعیت پروژه",
        "پروژه کجاست",
        "چقدر مونده",
        "مرحله فعلی",
        "الان کجای کاریم",
        "وضعیت کار"
    ]

    for word in status_words:
        if word in text:
            return "project_status"



    # پیشنهاد مرحله فعلی
    advice_words = [
        "الان چیکار کنم",
        "الان چکار کنم",
        "چی کار کنم",
        "چه کاری انجام بدم",
        "پیشنهاد بده",
        "راهنمایی کن"
    ]

    for word in advice_words:
        if word in text:
            return "project_advice"



    # گزارش تصمیم و تجربه
    decision_words = [
        "تصمیم گرفتم",
        "تصمیمم این بود",
        "انتخاب کردم",
        "راه حل این بود",
        "بعدش بهتر شد",
        "نتیجه این شد"
    ]

    for word in decision_words:
        if word in text:
            return "decision_report"



    # گزارش تجربه
    experience_words = [
        "مشکل از",
        "فهمیدم",
        "تجربه کردم",
        "یاد گرفتم",
        "متوجه شدم",
        "دفعه بعد"
    ]

    for word in experience_words:
        if word in text:
            return "experience_report"



    # شروع پروژه
    if (
        "میخواهم" in text
        or "می‌خواهم" in text
        or "پروژه" in text
    ):
        return "start_project"



    # مرحله بعد
    next_words = [
        "بعدی",
        "ادامه",
        "ادامه بده",
        "مرحله بعد"
    ]

    if text in next_words:
        return "next_step"



    # پایان مرحله
    done_words = [
        "انجام شد",
        "انجام دادم",
        "تمام شد",
        "تموم شد",
        "تمام کردم",
        "ساختم",
        "انتخاب کردم",
        "نصب کردم",
        "وصل کردم",
        "آماده شد"
    ]

    for word in done_words:
        if word in text:
            return "complete_step"



    return "normal"
