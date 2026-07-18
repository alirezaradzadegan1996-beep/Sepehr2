from decision_types import DecisionType


RULES = {

    DecisionType.PROJECT: [
        "پروژه",
        "برنامه",
        "اپلیکیشن",
        "بساز",
        "create",
        "project",
    ],

    DecisionType.CODE: [
        "کد",
        "python",
        "پایتون",
        "java",
        "cpp",
        "code",
    ],

    DecisionType.SEARCH: [
        "جستجو",
        "وب",
        "گوگل",
        "search",
    ],

    DecisionType.LEARNING: [
        "یاد بگیر",
        "آموزش",
        "learn",
    ],

    DecisionType.MEMORY: [
        "یادت",
        "حافظه",
        "remember",
    ],

    DecisionType.QUESTION: [
        "چی",
        "چرا",
        "چگونه",
        "کجا",
        "کی",
        "?",
        "؟",
    ],

    DecisionType.CHAT: [
        "سلام",
        "خداحافظ",
        "ممنون",
        "مرسی",
    ],
}
