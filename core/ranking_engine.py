def calculate_rank(item, similarity):

    feedback_score = item.get("score", 0)

    uses = item.get("uses", 0)


    rank = (
        similarity * 10
        +
        feedback_score
        +
        (uses * 0.5)
    )


    return rank




def choose_best(items):

    if not items:
        return None


    best = sorted(
        items,
        key=lambda x: x.get("rank", 0),
        reverse=True
    )


    return best[0]
