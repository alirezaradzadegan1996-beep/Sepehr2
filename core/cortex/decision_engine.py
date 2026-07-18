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

        if not scores:

            return DecisionResult(
                success=True,
                decision=Decision(
                    decision_type=DecisionType.CHAT.value,
                    confidence=0.50,
                    service="ChatService",
                    priority=1,
                    metadata={}
                ),
                message="Default chat decision."
            )

        winner = max(
            scores.items(),
            key=lambda item: item[1]["score"]
        )

        decision_type = winner[0]
        info = winner[1]

        decision = Decision(

            decision_type=decision_type.value,

            confidence=min(
                1.0,
                info["score"] / 3
            ),

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
            },
        )

        return DecisionResult(
            success=True,
            decision=decision,
            message="Decision created."
        )
