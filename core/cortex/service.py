"""
Base Cortex Service
"""


class Service:

    name = "service"

    def health(self):
        return {
            "status": "ok",
            "service": self.name,
        }
