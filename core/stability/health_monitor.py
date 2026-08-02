

class HealthMonitor:


    def check(self):

        return {

            "system":
                "healthy",

            "services":
                "running",

            "status":
                "HEALTH_MONITOR_ACTIVE"

        }


health_monitor = HealthMonitor()

