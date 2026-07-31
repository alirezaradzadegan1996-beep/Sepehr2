from core.capabilities import registry
from core.brain.self_map import self_map


class GoalObserver:


    def observe(self):

        abilities = registry.list()

        self_state = self_map.status()


        # ترکیب اطلاعات Registry و Self Model

        known = set(abilities)


        for item in self_state.get("abilities", {}):

            if item not in known:

                known.add(item)


        known = list(known)


        required = [
            "camera",
            "voice_input",
            "voice_output",
            "web",
            "tools"
        ]


        missing = [
            x for x in required
            if x not in known
        ]


        return {

            "abilities": known,

            "self_model": self_state,

            "missing": missing

        }



goal_observer = GoalObserver()
