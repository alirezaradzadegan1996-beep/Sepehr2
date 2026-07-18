from .decision_types import DecisionType


RULES = {

    DecisionType.PROJECT: {
        "پروژه": 3,
        "پروژه بساز": 5,
        "بساز": 2,
        "ساخت": 2,
        "ایجاد": 2,
        "اپ": 3,
        "اپلیکیشن": 3,
        "برنامه": 2,
        "فروشگاه": 4,
        "سایت": 3,
        "وبسایت": 3,
        "سیستم": 3,
        "create": 2,
        "project": 3,
    },


    DecisionType.CODE: {
        "کد": 2,
        "python": 3,
        "پایتون": 3,
        "java": 2,
        "cpp": 2,
        "code": 3,
    },


    DecisionType.SEARCH: {
        "جستجو": 3,
        "جستجو کن": 4,
        "وب": 2,
        "گوگل": 3,
        "اینترنت": 3,
        "search": 3,
    },


    DecisionType.LEARNING: {
        "یاد بگیر": 5,
        "آموزش": 3,
        "یادگیری": 3,
        "learn": 3,
    },


    DecisionType.MEMORY: {
        "یادت": 2,
        "حافظه": 4,
        "ذخیره کن": 3,
        "remember": 3,
    },


    DecisionType.QUESTION: {
        "چی": 1,
        "چرا": 2,
        "چگونه": 2,
        "کجا": 2,
        "کی": 1,
        "?": 1,
        "؟": 1,
    },


    DecisionType.CHAT: {
        "سلام": 3,
        "خداحافظ": 3,
        "ممنون": 2,
        "مرسی": 2,
    },
}
