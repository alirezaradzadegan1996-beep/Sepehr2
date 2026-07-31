class ActionBody:


    def execute(self, action):

        return {
            "action":action,
            "status":"executed"
        }



action_body = ActionBody()
