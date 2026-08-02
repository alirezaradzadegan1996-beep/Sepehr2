
from core.cognitive.long_term_planner import long_term_planner
from core.cognitive.concept_learning import concept_learning
from core.cognitive.self_model_awareness_upgrade import self_model_awareness_upgrade


def run():

    return {
        "planning":
            long_term_planner.plan("improve intelligence"),

        "learning":
            concept_learning.learn("reasoning"),

        "self_model":
            self_model_awareness_upgrade.inspect(),

        "status":"pass"
    }
