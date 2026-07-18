def detect_intent(text):

    text = text.strip().lower()


    # -------------------------
    # Teaching
    # -------------------------

    if text.startswith("یاد بگیر"):
        return "teaching"



    # -------------------------
    # Greeting
    # -------------------------

    greetings = [
        "سلام",
        "درود",
        "صبح بخیر",
        "شب بخیر"
    ]



    # -------------------------
    # Project
    # -------------------------

    project_words = [
        "پروژه",
        "اپ",
        "برنامه",
        "بساز",
        "طراحی کن",
        "ادامه پروژه",
        "وضعیت پروژه",
        "بعدی"
    ]



    # -------------------------
    # Memory
    # -------------------------

    memory_words = [
        "من کی هستم",
        "من کی‌ام",
        "درباره من",
        "اطلاعات من",
        "مشخصات من",
        "اسم",
        "ماشین",
        "شغل",
        "شهر",
        "رنگ",
        "سن",
        "چی از من می‌دونی",
        "چی می‌دونی",
        "حافظه",
        "فراموش کن",
        "تاریخچه",
        "آخرین سوال",
        "آخرین سوالام",
        "مکالمات",
        "صحبت های قبلی",
        "قبلا چی گفتیم"
    ]



    # -------------------------
    # Tools
    # -------------------------

    tool_words = [
        "ساعت",
        "تاریخ"
    ]



    search_words = [
        "جستجو",
        "جستجو کن",
        "در وب",
        "وب",
        "گوگل",
        "search",
    ]

    # -------------------------
    # Math
    # -------------------------

    math_words = [
        "+",
        "-",
        "*",
        "/",
        "چند میشه",
        "چقدر میشه",
        "حساب کن",
        "محاسبه کن"
    ]



    # -------------------------
    # Knowledge
    # -------------------------

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



    # -------------------------
    # Priority
    # -------------------------

    if text in greetings:
        return "greeting"


    for word in math_words:
        if word in text:
            return "math"



    for word in project_words:
        if word in text:
            return "project"



    for word in search_words:
        if word in text:
            return "search"



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
