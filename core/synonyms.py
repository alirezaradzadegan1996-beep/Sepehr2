SYNONYMS = {
    "مرکز": "پایتخت",
    "پایتخت": "پایتخت",

    "خودرو": "ماشین",
    "اتومبیل": "ماشین",

    "مملکت": "کشور",

    "کیست": "چه کسی است",
    "کیه": "چه کسی است"
}


def replace_synonyms(words):
    result = []

    for word in words:
        result.append(SYNONYMS.get(word, word))

    return result
