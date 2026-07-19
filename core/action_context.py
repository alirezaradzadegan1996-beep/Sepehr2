class ActionContext:
    def __init__(self):
        self.data = {}
        self.history = []
        self.variables = {}

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def add_history(self, action, result):
        self.history.append({
            "action": action,
            "result": result
        })

    def set_var(self, name, value):
        self.variables[name] = value

    def get_var(self, name, default=None):
        return self.variables.get(name, default)

    def export(self):
        return {
            "data": self.data,
            "variables": self.variables,
            "history": self.history
        }
