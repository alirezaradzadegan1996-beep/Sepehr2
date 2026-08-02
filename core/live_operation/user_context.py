

class UserContext:

    def load(self):
        return {
            "context":"persistent",
            "status":"PERSISTENT_USER_CONTEXT_ACTIVE"
        }


user_context=UserContext()

