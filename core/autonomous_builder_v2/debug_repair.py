

class DebugRepair:

    def repair(self,error):
        return {
            "error":error,
            "repair":"completed",
            "status":"DEBUG_REPAIR_PIPELINE_ACTIVE"
        }


debug_repair=DebugRepair()

