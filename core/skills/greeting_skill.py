NAME = "Greeting"

VERSION = "1.0"

DESCRIPTION = "سلام و احوالپرسی"


def score(text):

    greetings = [
        "سلام",
        "درود",
        "صبح بخیر",
        "ظهر بخیر",
        "عصر بخیر",
        "شب بخیر",
        "hi",
        "hello"
    ]

    text = text.lower()

    for word in greetings:
        if word in text:
            return 100

    return 0


def can_handle(text):

    return score(text) > 0


def run(text):

    return "سلام علیرضا ❤️ خوشحالم که دوباره با هم روی Sepehr2 کار می‌کنیم."
