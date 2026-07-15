def choose_best(candidates):

    if not candidates:

        return None



    priority = {

        "decision_memory": 5,

        "lesson_memory": 4,

        "experience_memory": 3,

        "smart_memory": 2,

        "topic_memory": 1,

        "knowledge": 0

    }



    for item in candidates:

        base_rank = item.get(
            "rank",
            0
        )


        bonus = priority.get(
            item.get("source"),
            0
        )


        item["final_rank"] = base_rank + bonus



    candidates.sort(
        key=lambda x: x.get(
            "final_rank",
            0
        ),
        reverse=True
    )



    print(
        "[THINKING] گزینه‌های موجود:"
    )


    for item in candidates:

        print(
            f"- {item['source']} | rank={item.get('rank')} | final={item.get('final_rank')}"
        )



    best = candidates[0]


    print(
        f"[THINKING] انتخاب شد: {best['source']}"
    )


    return best
