class WorkflowContext:
    """
    اطلاعات مشترک بین تمام Actionهای Workflow
    """

    def __init__(self, text, decision):
        self.text = text
        self.decision = decision

        self.data = {}
        self.results = []
        self.logs = []

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def add_result(self, result):
        self.results.append(result)

    def log(self, message):
        self.logs.append(message)

    def export(self):
        return {
            "text": self.text,
            "decision": self.decision.decision_type,
            "data": self.data,
            "results": self.results,
            "logs": self.logs
        }
