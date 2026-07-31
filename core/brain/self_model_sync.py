from core.brain.self_map import self_map
from core.capabilities import registry
from core.learning.priority_engine import learning_priority


class SelfModelSync:


    def sync(self):


        # abilities

        for ability in registry.list():

            self_map.add_ability(
                ability
            )


        # learning states

        for item in learning_priority.list():

            skill = item.get("skill")

            status = item.get("status")


            self_map.data["learning"][skill] = status


        self_map.save()


        return self_map.status()



self_model_sync = SelfModelSync()
