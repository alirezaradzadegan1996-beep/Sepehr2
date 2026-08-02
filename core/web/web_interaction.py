
class WebInteraction:

    def access(self, target):

        return {
            "target": target,
            "connection": "established",
            "data": "received",
            "status": "WEB_INTERACTION_ACTIVE"
        }


web_interaction = WebInteraction()
