class BodyState:

    def __init__(self):
        self.state = {
            "energy":"normal",
            "status":"active",
            "mode":"thinking"
        }


    def update(self, key, value):
        self.state[key] = value
        return self.state


    def get(self):
        return self.state


body_state = BodyState()
