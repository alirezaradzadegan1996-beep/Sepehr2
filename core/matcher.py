import re


STOP_WORDS = [
    "چقدر",
    "چند",
    "چیست",
    "چی",
    "است",
    "تا",
    "فاصله",
    "هست",
    "را",
    "رو",
    "در",
    "از",
    "به",
    "میشه",
    "میباشد",
    "؟",
    "?"
]


WEIGHTS = {
    "مساحت": 5,
    "جمعیت": 5,
    "پایتخت": 5,
    "خورشید": 5,
    "ماه": 5,
    "مریخ": 5,
    "سرعت": 4,
    "نور": 4,
    "فاصله": 1,
    "زمین": 1
}


def normalize(text):

    text = text.lower()

    for word in STOP_WORDS:
        text = text.replace(word, "")

    text = re.sub(r"\s+", " ", text).strip()

    return text



def similarity(text1, text2):

    text1 = normalize(text1)
    text2 = normalize(text2)

    words1 = set(text1.split())
    words2 = set(text2.split())

    score = 0

    for word in words1.intersection(words2):

        score += WEIGHTS.get(word, 1)

    return score
