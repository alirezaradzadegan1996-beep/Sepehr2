def detect_intent(text):

    text = text.strip().lower()

    # آموزش همیشه اولویت دارد
    if text.startswith("یاد بگیر"):
        return "teaching"

    greetings = [
        "سلام",
        "درود",
        "صبح بخیر",
        "شب بخیر"
    ]

    memory_words = [
        "اسم",
        "ماشین",
        "شغل",
        "شهر",
        "رنگ",
        "سن",
        "چی از من می‌دونی",
        "چی می‌دونی",
        "حافظه",
        "فراموش کن"
    ]

    tool_words = [
        "ساعت",
        "تاریخ"
    ]

    knowledge_words = [
        "چی",
        "چیه",
        "چیست",
        "کی",
        "کیه",
        "کجا",
        "کجاست",
        "چند",
        "چقد",
        "چطور",
        "چگونه",
        "چرا"
    ]

    knowledge_keywords = [
        "پایتخت",
        "مرکز",
        "ایران",
        "جمعیت",
        "سرعت",
        "نور",
        "فاصله",
        "دما",
        "سیاره",
        "زمین",
        "خورشید",
        "ماه"
    ]

    if text in greetings:
        return "greeting"

    for word in tool_words:
        if word in text:
            return "tool"

    for word in memory_words:
        if word in text:
            return "memory"

    for word in knowledge_words:
        if word in text:
            return "knowledge"

    for word in knowledge_keywords:
        if word in text:
            return "knowledge"

    return "chat"
