
class ActionExecutor:

    def execute(self, action):

        return {
            "action":action,
            "result":"completed",
            "status":"executed"
        }


action_executor = ActionExecutor()
