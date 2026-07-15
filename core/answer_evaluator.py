from core.smart_matcher import similarity


def keyword_score(question, answer):

    keywords = [
        "ربات",
        "پهپاد",
        "هوش مصنوعی",
        "دستیار",
        "مدار",
        "ماشین",
        "برنامه",
        "سیستم",
        "ساخت"
    ]


    score = 0


    for word in keywords:

        if word in question and word in answer:
            score += 1


    return score



def evaluate_answer(question, answer):


    sim = similarity(
        question,
        answer
    )


    key = keyword_score(
        question,
        answer
    )


    final_score = sim + key



    print(
        f"[ANSWER EVALUATOR] similarity={sim}"
    )

    print(
        f"[ANSWER EVALUATOR] keyword={key}"
    )



    if final_score >= 1:

        print(
            "[ANSWER EVALUATOR] good answer ✅"
        )

        return {
            "quality": "good",
            "score": final_score
        }


    print(
        "[ANSWER EVALUATOR] weak answer ⚠️"
    )


    return {
        "quality": "weak",
        "score": final_score
    }
