import json
import os

from core.topic_ranker import calculate_topic_rank


FILE = "data/topic_memory.json"


def load_topics():

    if not os.path.exists(FILE):
        return []

    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:
        return json.load(f)


def save_topics(data):

    with open(
        FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


def save_topic_memory(
    question,
    answer,
    topic
):

    data = load_topics()

    item = {
        "question": question,
        "answer": answer,
        "topic": topic,
        "uses": 1,
        "score": 0,
        "confidence": 1
    }

    data.append(item)

    save_topics(data)

    print("[TOPIC MEMORY] ذخیره شد 🧠")

    return item


def find_topic_answer(topic):

    data = load_topics()

    candidates = []

    for item in data:

        if item.get("topic") == topic:

            rank = calculate_topic_rank(item)

            candidate = {
                "source": "topic_memory",
                "question": item["question"],
                "answer": item["answer"],
                "topic": item["topic"],
                "uses": item.get("uses", 0),
                "score": item.get("score", 0),
                "confidence": item.get("confidence", 1),
                "rank": rank
            }

            candidates.append(candidate)


    if not candidates:
        return None


    candidates.sort(
        key=lambda x: x["rank"],
        reverse=True
    )

    best = candidates[0]

    print("[TOPIC MEMORY] بهترین تجربه موضوعی پیدا شد")
    print("Rank:", best["rank"])
    print("Uses:", best["uses"])

    return best
