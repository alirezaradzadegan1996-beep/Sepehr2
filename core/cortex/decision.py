from dataclasses import dataclass, field
from typing import Any


@dataclass
class Decision:

    # نوع تصمیم
    decision_type: str

    # میزان اطمینان
    confidence: float

    # سرویس مقصد
    service: str

    # آیا Planner نیاز است؟
    planner: bool = False

    # آیا Memory نیاز است؟
    requires_memory: bool = False

    # آیا Reasoning نیاز است؟
    requires_reasoning: bool = False

    # اولویت
    priority: int = 5

    # آیا اجرای فوری لازم است؟
    immediate: bool = False

    # اطلاعات تکمیلی
    metadata: dict[str, Any] = field(default_factory=dict)
