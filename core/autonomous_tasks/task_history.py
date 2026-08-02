
class TaskHistory:

    def save(self):
        return {
            "history":"saved",
            "status":"TASK_HISTORY_MEMORY_ACTIVE"
        }

task_history=TaskHistory()
