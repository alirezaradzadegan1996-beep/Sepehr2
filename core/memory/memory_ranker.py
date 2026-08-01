from datetime import datetime


class MemoryRanker:


    def score(self, item):

        score = 0


        score += item.get(
            "importance",
            0
        ) * 0.4


        score += item.get(
            "frequency",
            0
        ) * 0.2


        score += item.get(
            "confidence",
            0
        ) * 0.2


        if "last_access" in item:

            try:
                date = datetime.fromisoformat(
                    item["last_access"]
                )

                days = (
                    datetime.now() - date
                ).days

                score += max(
                    0,
                    1 - days/365
                ) * 0.2

            except Exception:
                pass


        return round(score,3)



    def rank(self, items):

        ranked = []

        for item in items:

            item = dict(item)

            item["memory_score"] = self.score(item)

            ranked.append(item)


        return sorted(
            ranked,
            key=lambda x:x["memory_score"],
            reverse=True
        )



memory_ranker = MemoryRanker()
