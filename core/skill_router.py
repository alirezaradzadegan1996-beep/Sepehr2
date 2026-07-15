from core.confidence import calculate_confidence



def choose_skill(text, skills):

    best_skill = None
    best_score = 0
    best_confidence = 0


    for skill in skills:

        try:

            if hasattr(skill, "score"):

                score = skill.score(text)

            elif skill.can_handle(text):

                score = 50

            else:

                score = 0


            confidence = calculate_confidence(score)


            print(
                f"[SKILL SCORE] {skill.NAME}: {score} | confidence={confidence}"
            )


            if confidence > best_confidence:

                best_confidence = confidence
                best_score = score
                best_skill = skill


        except Exception as e:

            print(
                f"[SKILL ERROR] {e}"
            )


    return best_skill, best_confidence
