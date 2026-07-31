from core.goals.manager import goal_manager


class GoalPlanner:


    def analyze(self, goal):

        plans = {


        "ساخت انسان دیجیتال": [

            {
             "name":"بینایی",
             "needs":["camera","vision"]
            },

            {
             "name":"شنوایی",
             "needs":["voice_input"]
            },

            {
             "name":"گفتار",
             "needs":["voice_output"]
            },

            {
             "name":"یادگیری",
             "needs":["memory","learning"]
            },

            {
             "name":"ارتباط با دنیا",
             "needs":["web","tools"]
            }

        ]

        }


        return {

            "goal":goal,

            "sub_goals":plans.get(
                goal,
                []
            )

        }



goal_planner = GoalPlanner()
