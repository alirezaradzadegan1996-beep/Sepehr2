
class HealthMonitor:

    def check(self):

        return {
            "brain": "ok",
            "memory": "ok",
            "tools": "ok",
            "agents": "ok",
            "status": "HEALTHY"
        }


health_monitor = HealthMonitor()
