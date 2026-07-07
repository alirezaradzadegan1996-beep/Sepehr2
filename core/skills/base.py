class Skill:
    def __init__(self, memory):
        self.memory = memory

    def run(self, data):
        raise NotImplementedError("Skill must implement run method")
