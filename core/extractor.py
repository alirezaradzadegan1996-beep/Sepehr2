from core.normalizer import normalize

STOP_WORDS = {
    "است",
    "هست",
    "بود",
    "را",
    "از",
    "به",
    "در",
    "که",
    "برای",
    "با",
    "این",
    "آن",
    "چیست",
    "چیه",
    "کجاست",
    "کجا",
    "کن",
    "بگو",
    "لطفا",
    "خواهش",
    "کشور"
}


def extract_keywords(text):
    text = normalize(text)

    words = text.split()

    result = []

    for word in words:
        if word and word not in STOP_WORDS:
            result.append(word)

    return result
