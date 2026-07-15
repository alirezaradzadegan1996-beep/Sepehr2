def calculate_topic_rank(item):

    uses = item.get(
        "uses",
        0
    )


    score = item.get(
        "score",
        0
    )


    confidence = item.get(
        "confidence",
        1
    )


    rank = (
        uses * 2
        +
        score
        +
        confidence
    )


    return rank
