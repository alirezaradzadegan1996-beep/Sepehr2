from .decision import Decision
from .decision_result import DecisionResult
from .decision_rules import RULES
from .decision_types import DecisionType


class DecisionEngine:

    def decide(self, text: str) -> DecisionResult:

        text = text.lower().strip()

        for decision_type, keywords in RULES.items():

            for keyword in keywords:

                if keyword.lower() in text:

                    decision = Decision(
                        decision_type=decision_type.value,
                        confidence=0.90,
                        service=f"{decision_type.value.title()}Service",
                    )

                    return DecisionResult(
                        success=True,
                        decision=decision,
                    )

        return DecisionResult(
            success=True,
            decision=Decision(
                decision_type=DecisionType.CHAT.value,
                confidence=0.50,
                service="ChatService",
            ),
        )
