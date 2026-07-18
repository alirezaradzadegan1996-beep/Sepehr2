from dataclasses import dataclass, field
from typing import Any


@dataclass
class Decision:
    decision_type: str
    confidence: float
    service: str

    planner: bool = False
    requires_memory: bool = False
    requires_reasoning: bool = False

    metadata: dict[str, Any] = field(default_factory=dict)
