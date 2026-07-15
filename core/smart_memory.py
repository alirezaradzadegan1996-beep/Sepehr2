import json
import os

from core.smart_matcher import similarity
from core.ranking_engine import calculate_rank
from core.confidence import should_use_memory


FILE = "data/learning_score.json"


def load_memory():

    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def find_best_answer(question):

    data = load_memory()

    if not data:
        return None


    candidates = []


    for item in data:

        sim = similarity(
            question,
            item["question"]
        )

        if should_use_memory(sim):

            rank = calculate_rank(
                item,
                sim
            )

            candidate = {
                "source": "smart_memory",
                "question": item["question"],
                "answer": item["answer"],
                "score": item.get("score", 0),
                "uses": item.get("uses", 0),
                "rank": rank
            }

            candidates.append(candidate)


    if not candidates:

        print("[SMART MEMORY] تجربه مناسب پیدا نشد")

        return None


    candidates.sort(
        key=lambda x: x["rank"],
        reverse=True
    )


    best = candidates[0]


    print("[SMART MEMORY] بهترین تجربه انتخاب شد")
    print("Rank:", best["rank"])
    print("Score:", best["score"])
    print("Uses:", best["uses"])


    return best
