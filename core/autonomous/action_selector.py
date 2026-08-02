
class ActionSelector:
    def select(self, actions):
        return actions[0] if actions else None

action_selector = ActionSelector()
