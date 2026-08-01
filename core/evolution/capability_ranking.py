
from core.evolution.capability_performance import capability_performance

class CapabilityRanking:

    def rank(self):

        scores = []

        for name in capability_performance.data.keys():

            stat = capability_performance.get(name)

            scores.append({
                "capability": name,
                "score": stat.get("score", 0),
                "uses": stat.get("uses", 0),
                "success": stat.get("success", 0)
            })

        scores.sort(
            key=lambda x: (
                x["score"],
                x["uses"],
                x["success"]
            ),
            reverse=True
        )

        return scores


ranking = CapabilityRanking()
