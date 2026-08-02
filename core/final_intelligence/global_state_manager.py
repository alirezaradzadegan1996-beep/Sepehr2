

class GlobalStateManager:


    def manage(self, state):

        return {

            "state":
                state,

            "monitoring":
                "active",

            "status":
                "GLOBAL_STATE_MANAGER_ACTIVE"

        }



global_state_manager = GlobalStateManager()

