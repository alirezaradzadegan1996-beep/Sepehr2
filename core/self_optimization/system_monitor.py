

class SystemMonitor:


    def monitor(self, system):

        return {

            "system":
                system,

            "health":
                "checked",

            "status":
                "SYSTEM_MONITOR_ACTIVE"

        }



system_monitor = SystemMonitor()

