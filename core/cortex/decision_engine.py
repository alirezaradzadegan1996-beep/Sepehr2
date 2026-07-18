from .decision import Decision
from .decision_result import DecisionResult
from .decision_rules import RULES
from .decision_types import DecisionType


class DecisionEngine:
    """Cortex Decision Engine"""

    def decide(self, text: str) -> DecisionResult:

        if not text:
            return DecisionResult(
                success=False,
                message="Empty input."
            )

        original_text = text
        text = text.lower().strip()

        for decision_type, keywords in RULES.items():

            for keyword in keywords:

                if keyword.lower() in text:

                    decision = Decision(
                        decision_type=decision_type.value,
                        confidence=0.90,
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

                        priority=5,
                        immediate=False,

                        metadata={
                            "matched_keyword": keyword,
                            "original_text": original_text,
                        },
                    )

                    return DecisionResult(
                        success=True,
                        decision=decision,
                        message="Decision created."
                    )

        return DecisionResult(
            success=True,
            decision=Decision(
                decision_type=DecisionType.CHAT.value,
                confidence=0.50,
                service="ChatService",

                planner=False,
                requires_memory=False,
                requires_reasoning=False,

                priority=1,
                immediate=False,

                metadata={
                    "matched_keyword": None,
                    "original_text": original_text,
                },
            ),
            message="Default chat decision."
        )
