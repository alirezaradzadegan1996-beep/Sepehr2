from core.brain.self_map import self_map
from core.capabilities.loader import discover
from core.capabilities import registry
from core.learning.priority_engine import learning_priority


class SelfAwareness:


    def sync(self):

        discover()


        for ability in registry.list():

            self_map.add_ability(
                ability
            )


    def analyze(self):

        self.sync()


        return {

            "abilities": registry.list(),

            "learning_queue": learning_priority.list(),

            "self_map": self_map.status()

        }



    def status(self):

        return self.analyze()



self_awareness = SelfAwareness()
