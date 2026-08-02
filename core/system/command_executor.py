
class CommandExecutor:

    def execute(self, command):

        return {
            "command": command,
            "result": "executed",
            "status": "success"
        }


command_executor = CommandExecutor()
