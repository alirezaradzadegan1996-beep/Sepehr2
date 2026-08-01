from core.memory.goal_completion_memory import goal_completion_memory
from core.brain.self_map import self_map


class GoalFilter:


    def filter(self, goals):

        result = []


        self_state = self_map.status()

        abilities = self_state.get(
            "abilities",
            {}
        )


        for goal in goals:

            skill = goal.get("skill")


            completed = (
                goal_completion_memory.exists(skill)
                or skill in abilities
            )


            if not completed:

                result.append(goal)


        return result



goal_filter = GoalFilter()
