from .decision_rules import RULES


class DecisionScorer:
    """
    مسئول محاسبه امتیاز هر نوع تصمیم
    """

    def score(self, text: str) -> dict:
        text = text.lower().strip()

        scores = {}

        for decision_type, keywords in RULES.items():

            score = 0
            matched = []

            for keyword in keywords:

                if keyword.lower() in text:
                    score += 1
                    matched.append(keyword)

            if score > 0:
                scores[decision_type] = {
                    "score": score,
                    "matched": matched,
                }

        return scores
