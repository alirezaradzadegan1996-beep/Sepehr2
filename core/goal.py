import uuid
from datetime import datetime


class Goal:

    def __init__(self, text):

        self.id = str(uuid.uuid4())[:8]

        self.text = text

        self.status = "new"

        self.current_step = 0

        self.steps = []

        self.result = None

        self.logs = []

        self.created_at = datetime.now()

    def add_step(self, step):

        self.steps.append(step)

    def next_step(self):

        if self.current_step < len(self.steps):
            step = self.steps[self.current_step]
            self.current_step += 1
            return step

        return None

    def add_log(self, message):

        self.logs.append({
            "time": datetime.now(),
            "message": message
        })

    def finish(self, result):

        self.status = "completed"

        self.result = result
