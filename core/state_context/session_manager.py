

class SessionManager:

    def create(self,user):
        return {
            "user":user,
            "session":"created",
            "status":"SESSION_MANAGER_ACTIVE"
        }


session_manager=SessionManager()

