from .decision import Decision
from .decision_result import DecisionResult
from .decision_scorer import DecisionScorer
from .decision_types import DecisionType


class DecisionEngine:
    """
    Cortex Decision Engine
    """

    def __init__(self):
        self.scorer = DecisionScorer()


    def decide(self, text: str) -> DecisionResult:

        if not text:
            return DecisionResult(
                success=False,
                message="Empty input."
            )


        scores = self.scorer.score(text)


        # اگر چیزی تشخیص داده نشد
        if not scores:
            return DecisionResult(
                success=True,
                decision=Decision(
                    decision_type=DecisionType.CHAT.value,
                    confidence=0.50,
                    service="ChatService",
                    priority=1,
                    metadata={
                        "original_text": text
                    }
                ),
                message="Default chat decision."
            )


        # انتخاب بالاترین امتیاز
        winner = max(
            scores.items(),
            key=lambda item: item[1]["score"]
        )


        decision_type = winner[0]
        info = winner[1]


        # محاسبه confidence
        total_score = sum(
            item["score"]
            for item in scores.values()
        )


        confidence = round(
            info["score"] / total_score,
            2
        ) if total_score else 0.5



        decision = Decision(

            decision_type=decision_type.value,

            confidence=confidence,

            service=f"{decision_type.value.title()}Service",


            planner=decision_type in (
                DecisionType.PROJECT,
                DecisionType.PLAN,
            ),


            requires_memory=decision_type in (
                DecisionType.MEMORY,
                DecisionType.LEARNING,
            ),


            requires_reasoning=decision_type in (
                DecisionType.REASONING,
                DecisionType.QUESTION,
            ),


            priority=info["score"],


            metadata={
                "scores": scores,
                "matched_keywords": info["matched"],
                "original_text": text,
            }
        )


        return DecisionResult(
            success=True,
            decision=decision,
            message="Decision created."
        )
