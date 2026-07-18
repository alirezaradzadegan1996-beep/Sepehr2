from enum import Enum


class DecisionType(str, Enum):
    CHAT = "chat"
    QUESTION = "question"
    SEARCH = "search"
    PROJECT = "project"
    MEMORY = "memory"
    LEARNING = "learning"
    CODE = "code"
    REASONING = "reasoning"
    PLAN = "plan"
    SYSTEM = "system"
    UNKNOWN = "unknown"
