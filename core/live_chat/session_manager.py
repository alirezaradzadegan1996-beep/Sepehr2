
class SessionManager:

    def create(self):
        return {
            "session":"created",
            "status":"CHAT_SESSION_MANAGER_ACTIVE"
        }

session_manager=SessionManager()
