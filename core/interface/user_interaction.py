
class UserInteraction:

    def handle(self, message):

        return {
            "input": message,
            "context": "loaded",
            "response": "generated",
            "status": "USER_INTERACTION_ACTIVE"
        }


user_interaction = UserInteraction()
