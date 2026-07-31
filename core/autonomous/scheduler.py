class AutonomousScheduler:


    def __init__(self):
        self.tasks=[]


    def add(self, task):

        self.tasks.append(task)

        return {
            "task":task,
            "status":"scheduled"
        }


    def list(self):

        return self.tasks



autonomous_scheduler = AutonomousScheduler()
