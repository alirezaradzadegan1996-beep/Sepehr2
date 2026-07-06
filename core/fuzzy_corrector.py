import difflib

VOCAB = [
    "پایتخت",
    "مرکز",
    "جمعیت",
    "سرعت",
    "نور",
    "کشور",
    "ایران",
    "تهران",
    "دما",
    "فاصله",
    "جرم"
]


def best_match(word):

    match = difflib.get_close_matches(word, VOCAB, n=1, cutoff=0.6)

    if match:
        return match[0]

    return word


def correct_text(text):

    words = text.split()

    return " ".join(best_match(w) for w in words)
