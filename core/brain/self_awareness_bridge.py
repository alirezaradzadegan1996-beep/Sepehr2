
from core.brain.self_identity import self_identity
from core.brain.self_state import self_state
from core.brain.self_model import self_model


class SelfAwarenessBridge:

    def analyze(self):
        return {
            "identity":self_identity.get(),
            "state":self_state.analyze(),
            "model":self_model.build(),
            "status":"aware"
        }


self_awareness_bridge = SelfAwarenessBridge()
