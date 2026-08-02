
class EnvironmentModel:

    def update(self, data):
        return {
            "environment": data,
            "status": "updated"
        }

environment_model = EnvironmentModel()
