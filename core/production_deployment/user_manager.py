

class UserManager:

    def authorize(self):
        return {
            "user":"authorized",
            "status":"USER_ACCESS_MANAGER_ACTIVE"
        }


user_manager=UserManager()

