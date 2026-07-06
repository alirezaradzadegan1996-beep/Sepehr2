CORRECTIONS = {
    # مهم‌ترین خطاها
    "پاتخت": "پایتخت",
    "مرمز": "مرکز",
    "سرعط": "سرعت",
    "جمعت": "جمعیت",
    "کشورای": "کشورهای",
    "دماا": "دما",
    "فاصل": "فاصله",

    # غلط‌های رایج
    "چندتاست": "چند تاست",
    "کجاس": "کجاست",
    "چیهه": "چیه",
}


def correct_word(word):

    return CORRECTIONS.get(word, word)


def correct_text(text):

    words = text.split()

    corrected = [
        correct_word(w)
        for w in words
    ]

    return " ".join(corrected)
