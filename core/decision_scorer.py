def calculate_score(item):

    score = 0


    # استفاده بیشتر = اعتماد بیشتر

    score += item.get(
        "uses",
        1
    )


    result = item.get(
        "result",
        ""
    )


    success_words = [
        "موفق",
        "بهتر شد",
        "درست شد",
        "حل شد",
        "کار کرد",
        "پرواز موفق"
    ]


    fail_words = [
        "خراب شد",
        "مشکل داشت",
        "جواب نداد",
        "ناموفق"
    ]


    for word in success_words:

        if word in result:

            score += 10
            break



    for word in fail_words:

        if word in result:

            score -= 5
            break



    return score



def rank_decisions(data):

    results = []


    for item in data:

        item["score"] = calculate_score(item)

        results.append(item)



    results.sort(
        key=lambda x: x.get(
            "score",
            0
        ),
        reverse=True
    )


    return results
