from dataclasses import dataclass
from typing import Optional

from decision import Decision


@dataclass
class DecisionResult:
    success: bool
    decision: Optional[Decision] = None
    message: str = ""
