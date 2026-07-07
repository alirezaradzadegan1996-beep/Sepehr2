import re

def normalize(text):
    text = text.strip().lower()

    replacements = {
        "ي": "ی",
        "ك": "ک",
        "می ": "می‌",
        "میدونی": "می‌دونی",
        "نمیدونی": "نمی‌دونی",
        "چیه": "چیست",
        "رو": "را",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # حذف فاصله‌های اضافی
    text = re.sub(r"\s+", " ", text)

    # حذف علائم نگارشی
    for ch in "؟?!،,:؛.\"'()[]{}":
        text = text.replace(ch, "")

    return text.strip()
