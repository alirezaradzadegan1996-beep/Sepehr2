import json
import os

from core.topic_classifier import detect_topic
from core.lesson_recall import recall_lesson


FILE = "data/plans.json"



def load_plans():

    if not os.path.exists(FILE):

        return {}


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)




def create_plan(text):

    topic = detect_topic(text)


    plans = load_plans()


    if topic not in plans:

        return None



    lesson = recall_lesson(
        topic
    )


    return {
        "topic": topic,
        "steps": plans[topic],
        "previous_lesson": lesson
    }
