

class StateManager:

    def update(self,data):

        return {
            "state":"updated",
            "data":data,
            "status":"STATE_MANAGEMENT_ACTIVE"
        }


state_manager=StateManager()

