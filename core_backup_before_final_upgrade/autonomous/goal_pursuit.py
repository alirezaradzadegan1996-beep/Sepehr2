class GoalPursuit:


    def __init__(self):
        self.goals=[]


    def pursue(self, goal):

        self.goals.append(goal)

        return {
            "goal":goal,
            "status":"in_progress"
        }


    def status(self):
        return self.goals



goal_pursuit = GoalPursuit()
