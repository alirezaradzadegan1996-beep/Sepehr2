# core/knowledge_router.py

def detect_category(text):
    """
    تشخیص شاخه دانش از روی متن
    """

    text = text.lower()

    categories = {

        "astronomy": [
            "سیاره", "خورشید", "ماه", "ستاره", "کهکشان",
            "منظومه", "مشتری", "مریخ", "زحل", "فضا"
        ],

        "mathematics": [
            "ریاضی", "جمع", "تفریق", "ضرب", "تقسیم",
            "معادله", "مثلث", "انتگرال", "مشتق"
        ],

        "physics": [
            "فیزیک", "نیرو", "سرعت", "نور", "گرانش",
            "انرژی", "حرکت"
        ],

        "chemistry": [
            "شیمی", "اتم", "مولکول", "عنصر",
            "اسید", "باز"
        ],

        "biology": [
            "زیست", "سلول", "گیاه", "جانور",
            "DNA"
        ],

        "medicine": [
            "بیماری", "دارو", "قلب", "مغز",
            "کبد", "پزشکی"
        ],

        "programming": [
            "پایتون", "python", "کدنویسی",
            "برنامه نویسی", "جاوا", "html",
            "css", "api"
        ],

        "business": [
            "شرکت", "کسب و کار", "بیزینس",
            "کارخانه"
        ],

        "accounting": [
            "حسابداری", "مالی", "فاکتور",
            "حقوق", "دستمزد"
        ],

        "marketing": [
            "تبلیغ", "بازاریابی", "فروش",
            "کمپین", "مشتری"
        ],

        "construction": [
            "ساختمان", "بتن", "آجر",
            "نقشه", "معماری"
        ],

        "language": [
            "فعل", "فاعل", "مفعول",
            "دستور زبان", "ادبیات"
        ],

        "history": [
            "تاریخ", "جنگ", "شاه",
            "هخامنشی", "ساسانی"
        ]

    }

    for category, words in categories.items():

        for word in words:

            if word in text:
                return category

    return "general"

def detect_all_categories(text):
    """
    تمام شاخه‌های مرتبط را برمی‌گرداند.
    """

    text = text.lower()

    categories = {

        "astronomy": [
            "سیاره","خورشید","ماه","ستاره","فضا","منظومه","مریخ","مشتری"
        ],

        "mathematics": [
            "ریاضی","جمع","تفریق","ضرب","تقسیم","انتگرال","معادله"
        ],

        "physics": [
            "نور","سرعت","گرانش","انرژی","نیرو","حرکت"
        ],

        "programming": [
            "برنامه","اپ","نرم افزار","پایتون","کدنویسی","html","api"
        ],

        "business": [
            "شرکت","کارخانه","کسب و کار","بیزینس"
        ],

        "accounting": [
            "مالی","حسابداری","فاکتور","حقوق","دستمزد"
        ],

        "marketing": [
            "تبلیغ","بازاریابی","فروش","مشتری"
        ],

        "construction": [
            "ساختمان","نقشه","معماری","بتن"
        ],

        "medicine": [
            "بیماری","دارو","قلب","پزشکی"
        ]

    }

    result = []

    for category, words in categories.items():

        for word in words:

            if word in text:

                result.append(category)

                break

    if not result:

        result.append("general")

    return result
