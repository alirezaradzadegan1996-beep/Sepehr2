from dataclasses import dataclass
from typing import List


@dataclass
class Action:
    name: str
    service: str
    payload: dict


class ActionChainBuilder:

    def build(self, decision) -> List[Action]:

        chain = []

        intent = getattr(decision, "intent", None)

        if intent == "create_project":

            chain.extend([
                Action("analyze", "project", {}),
                Action("plan", "project", {}),
                Action("generate", "project", {}),
                Action("test", "project", {}),
                Action("fix", "project", {}),
                Action("save", "memory", {})
            ])

        elif intent == "analyze_file":

            chain.extend([
                Action("load", "file", {}),
                Action("analyze", "reasoning", {}),
                Action("summary", "reasoning", {}),
                Action("save", "memory", {})
            ])

        elif intent == "chat":

            chain.append(
                Action("respond", "chat", {})
            )

        else:

            chain.append(
                Action("fallback", "chat", {})
            )

        return chain
