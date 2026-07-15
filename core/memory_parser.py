import re


def parse_memory(text):

    text = text.strip()

    # سوال‌ها ذخیره نشوند
    question_words = [
        "چیه",
        "چیست",
        "چی هست",
        "چقدر",
        "چند",
        "؟",
        "?"
    ]

    for word in question_words:
        if word in text:
            return None

    # حالت "علیرضاست" → "علیرضا است"
    text = re.sub(r"([اآبپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی])ست$", r"\1 است", text)

    patterns = [

        # اسم
        (r"^اسم من\s+(.+?)\s+است$", "name"),
        (r"^من اسمم\s+(.+?)\s+است$", "name"),

        # شهر
        (r"^شهر من\s+(.+?)\s+است$", "city"),
        (r"^من اهل\s+(.+?)\s+هستم$", "city"),

        # شغل
        (r"^شغل من\s+(.+?)\s+است$", "job"),
        (r"^شغلم\s+(.+?)\s+است$", "job"),

        # سن
        (r"^سن من\s+(\d+)\s*ساله\s*است$", "age"),
        (r"^سنم\s+(\d+)\s*ساله\s*است$", "age"),

        # رنگ
        (r"^رنگ مورد علاقه من\s+(.+?)\s+است$", "favorite_color"),

        # علاقه
        (r"^علاقه من\s+(.+?)\s+است$", "interests"),

        # هدف
        (r"^هدف من\s+(.+?)\s+است$", "goals"),
    ]

    for pattern, key in patterns:

        m = re.match(pattern, text)

        if not m:
            continue

        value = m.group(1).strip()

        if key in ["interests", "goals"]:
            return {
                "key": key,
                "value": [value]
            }

        return {
            "key": key,
            "value": value
        }

    return None
