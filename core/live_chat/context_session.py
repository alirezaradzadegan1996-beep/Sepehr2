
class ContextSession:

    def load(self):
        return {
            "context":"loaded",
            "status":"CONTEXT_SESSION_MANAGER_ACTIVE"
        }

context_session=ContextSession()
