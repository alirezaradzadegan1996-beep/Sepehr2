def rank_experiences(experiences):

    if not experiences:

        return None



    for exp in experiences:

        uses = exp.get(
            "uses",
            1
        )

        score = uses


        # تجربه‌هایی که راه‌حل دارند ارزش بیشتری دارند

        if exp.get("solution"):

            score += 2


        exp["score"] = score



    experiences.sort(
        key=lambda x: x.get("score", 0),
        reverse=True
    )


    return experiences[0]
