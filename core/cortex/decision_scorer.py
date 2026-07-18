from .decision_rules import RULES


class DecisionScorer:
    """
    محاسبه امتیاز تصمیم‌ها با وزن کلمات
    """

    def score(self, text: str) -> dict:

        text = text.lower().strip()

        scores = {}

        for decision_type, keywords in RULES.items():

            score = 0
            matched = []

            for keyword, weight in keywords.items():

                if keyword.lower() in text:
                    score += weight
                    matched.append(keyword)

            if score > 0:
                scores[decision_type] = {
                    "score": score,
                    "matched": matched,
                }

        return scores
