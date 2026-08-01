from core.brain.self_map import self_map


class SelfModelUpdater:


    def update(self, capability):


        self_map.add_ability(
            capability
        )


        self_map.complete_learning(
            capability
        )


        return {

            "capability": capability,

            "status":"registered"

        }



    def status(self):

        return self_map.status()



self_model_updater = SelfModelUpdater()
