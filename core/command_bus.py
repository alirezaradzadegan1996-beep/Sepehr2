from core.router import route
from core.intent import detect_intent


def execute(task):

    intent = detect_intent(task)

    return route(intent, task)
