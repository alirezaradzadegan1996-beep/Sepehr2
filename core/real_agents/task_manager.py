

class TaskManager:

    def execute(self,task):
        return {
            "task":task,
            "execution":"completed",
            "status":"TASK_EXECUTION_MANAGER_ACTIVE"
        }


task_manager=TaskManager()

