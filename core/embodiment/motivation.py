class MotivationState:


    def __init__(self):
        self.goal=None


    def set_goal(self, goal):
        self.goal=goal

        return {
            "goal":self.goal,
            "status":"active"
        }


    def get_goal(self):
        return self.goal



motivation_state = MotivationState()
