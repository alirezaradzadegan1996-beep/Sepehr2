from .decision import Decision
from .decision_result import DecisionResult
from .decision_scorer import DecisionScorer
from .decision_types import DecisionType
from .decision_features import detect_features
from .decision_priority import PRIORITY_BONUS
SERVICE_MAP = {
    DecisionType.CHAT: "router",
    DecisionType.QUESTION: "router",
    DecisionType.SEARCH: "search",
    DecisionType.PROJECT: "ProjectService",
    DecisionType.MEMORY: "memory",
    DecisionType.LEARNING: "memory",
    DecisionType.REASONING: "reasoning",
    DecisionType.PLAN: "planner",
    DecisionType.SYSTEM: "router",
    DecisionType.UNKNOWN: "router",
}

class DecisionEngine:
    """
    Cortex Decision Engine
    موتور تصمیم‌گیری اصلی Sepehr2
    """

    def __init__(self):
        self.scorer = DecisionScorer()


    def decide(self, text: str) -> DecisionResult:

        if not text:
            return DecisionResult(
                success=False,
                message="Empty input."
            )


        # -------------------------
        # Feature Detection
        # -------------------------

        features = detect_features(text)


        # -------------------------
        # Score
        # -------------------------

        scores = self.scorer.score(text)


        if not scores:
            return DecisionResult(
                success=True,
                decision=Decision(
                    decision_type=DecisionType.CHAT.value,
                    confidence=0.50,
                    service="ChatService",
                    priority=1,
                    metadata={
                        "features": features
                    }
                ),
                message="Default chat decision."
            )


        # -------------------------
        # Apply Priority Bonus
        # -------------------------

        ranked = {}

        for decision_type, info in scores.items():

            bonus = PRIORITY_BONUS.get(
                decision_type,
                0
            )

            ranked[decision_type] = (
                info["score"] + bonus
            )


        # -------------------------
        # Select Winner
        # -------------------------

        winner_type = max(
            ranked,
            key=ranked.get
        )


        info = scores[winner_type]


        total = sum(
            ranked.values()
        )


        confidence = round(
            ranked[winner_type] / total,
            2
        ) if total else 0.5



        # -------------------------
        # Create Decision
        # -------------------------

        decision = Decision(

            decision_type=winner_type.value,

            confidence=confidence,

            service=SERVICE_MAP.get(
                winner_type,
                "router",
            ),

            planner=winner_type in (
                DecisionType.PROJECT,
                DecisionType.PLAN,
            ),

            requires_memory=winner_type in (
                DecisionType.MEMORY,
                DecisionType.LEARNING,
            ),

            requires_reasoning=winner_type in (
                DecisionType.REASONING,
                DecisionType.QUESTION,
            ),

            priority=ranked[winner_type],

            metadata={

                "scores": scores,

                "priority_scores": ranked,

                "matched_keywords":
                    info["matched"],

                "features":
                    features,

                "original_text":
                    text
            }
        )


        return DecisionResult(

            success=True,

            decision=decision,

            message="Decision created."

        )
