

class StateRecovery:

    def recover(self,state):
        return {
            "state":state,
            "recovery":"completed",
            "status":"STATE_RECOVERY_ACTIVE"
        }


state_recovery=StateRecovery()

