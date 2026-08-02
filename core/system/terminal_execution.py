
class TerminalExecution:

    def run(self, command):

        return {
            "command": command,
            "result": "executed",
            "status": "TERMINAL_EXECUTION_ACTIVE"
        }


terminal_execution = TerminalExecution()
