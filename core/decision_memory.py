import json
import os

from core.decision_scorer import rank_decisions


FILE = "data/decision_memory.json"



def load_decisions():

    if not os.path.exists(FILE):
        return []


    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def save_decisions(data):

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



def save_decision(
    project,
    stage,
    problem,
    decision,
    result=""
):

    data = load_decisions()


    item = {
        "project": project,
        "stage": stage,
        "problem": problem,
        "decision": decision,
        "result": result,
        "uses": 1
    }


    data.append(item)


    save_decisions(data)


    print(
        "[DECISION MEMORY] تصمیم ذخیره شد 🧠"
    )


    return item



def find_decision(stage):

    data = load_decisions()


    results = []


    for item in data:

        if item.get("stage") == stage:

            item["uses"] = item.get(
                "uses",
                1
            ) + 1


            results.append(item)



    if not results:

        return None



    # رتبه‌بندی هوشمند تصمیم‌ها

    ranked = rank_decisions(results)



    best = ranked[0]


    save_decisions(data)


    print(
        "[DECISION MEMORY] بهترین تصمیم انتخاب شد 🧠"
    )


    return best
