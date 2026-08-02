
class TaskInterpreter:

    def understand(self,task):
        return {
            "task":"understood",
            "status":"USER_TASK_INTERPRETER_ACTIVE"
        }

task_interpreter=TaskInterpreter()
