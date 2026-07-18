from .decision_types import DecisionType


PRIORITY_BONUS = {

    DecisionType.PROJECT: 10,

    DecisionType.CODE: 5,

    DecisionType.SEARCH: 4,

    DecisionType.LEARNING: 3,

    DecisionType.MEMORY: 0,

    DecisionType.QUESTION: 0,

    DecisionType.CHAT: 0,

}
