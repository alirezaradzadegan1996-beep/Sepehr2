

class GenesisStateCreator:


    def create(self, system):

        return {

            "system":
                system,

            "state":
                "created",

            "status":
                "GENESIS_STATE_ACTIVE"

        }



genesis_state_creator = GenesisStateCreator()

