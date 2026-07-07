# دسته‌بندی مفهومی ساده برای شروع

CATEGORY_MAP = {
    "geography": [
        "پایتخت",
        "مرکز",
        "کشور",
        "شهر",
        "ایران",
        "تهران",
        "جمعیت"
    ],

    "physics": [
        "سرعت",
        "نور",
        "جرم",
        "انرژی",
        "دما"
    ],

    "general": [
        "چی",
        "کجاست",
        "چیه",
        "کی",
        "چطور"
    ]
}


def detect_category(text):

    text = text.strip()

    scores = {}

    for category, words in CATEGORY_MAP.items():

        score = 0

        for w in words:
            if w in text:
                score += 1

        if score > 0:
            scores[category] = score

    if not scores:
        return "unknown"

    return max(scores, key=scores.get)
