from modules.clock import run as clock_run

SKILLS = {
    "ساعت": clock_run,
}


def run_skill(text):

    for keyword, func in SKILLS.items():
        if keyword in text:
            return func()

    return None
