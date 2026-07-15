import json

from core.matcher import similarity
from core.confidence_manager import increase_confidence
from core.knowledge_ranker import calculate_rank


KNOWLEDGE_FILE = "data/knowledge.json"
CONSOLIDATED_FILE = "data/consolidated_knowledge.json"



def load_knowledge():

    try:

        with open(
            KNOWLEDGE_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return {}




def load_consolidated():

    try:

        with open(
            CONSOLIDATED_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        result = {}


        for item in data:

            result[item["question"]] = item["answer"]


        return result


    except Exception:

        return {}




def save_knowledge(data):

    with open(
        KNOWLEDGE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )




def search_knowledge(text):

    data = load_knowledge()


    # اضافه کردن دانش ساخته شده از تجربه
    consolidated = load_consolidated()

    data.update(consolidated)



    candidates = []


    print(f"[AFTER NORMALIZE]: '{text}'")



    for key, item in data.items():

        score = similarity(
            text,
            key
        )


        confidence = 1


        if isinstance(item, dict):

            confidence = item.get(
                "confidence",
                1
            )



        rank = calculate_rank(
            score,
            confidence
        )



        print(
            f"[DEBUG MATCH] {key} | score={score} | confidence={confidence} | rank={rank}"
        )



        if score >= 3:

            candidates.append(
                {
                    "key": key,
                    "score": score,
                    "rank": rank,
                    "item": item
                }
            )



    if not candidates:

        print("[Knowledge Rank]: No candidate")

        return None




    candidates.sort(
        key=lambda x: x["rank"],
        reverse=True
    )



    best = candidates[0]



    print(
        f"[BEST KNOWLEDGE]: {best['key']} | rank={best['rank']}"
    )



    increase_confidence(
        best["key"]
    )



    item = best["item"]



    if isinstance(item, dict):

        print(
            f"[Confidence]: {item.get('confidence',1)}"
        )

        return item.get("answer")



    return item




def learn_knowledge(text, answer):

    data = load_knowledge()


    data[text] = answer


    save_knowledge(data)


    return True
