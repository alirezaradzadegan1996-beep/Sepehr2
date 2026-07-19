class ActionResult:
    def __init__(
        self,
        success=True,
        output=None,
        error=None,
        metadata=None
    ):
        self.success = success
        self.output = output
        self.error = error
        self.metadata = metadata or {}

    def to_dict(self):
        return {
            "success": self.success,
            "output": self.output,
            "error": self.error,
            "metadata": self.metadata
        }
