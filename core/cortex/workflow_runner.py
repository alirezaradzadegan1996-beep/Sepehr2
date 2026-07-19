class WorkflowRunner:
    """
    اجرای مرحله به مرحله Workflow
    """

    def __init__(self):
        self.actions = []

    def add(self, action):
        self.actions.append(action)
        self.actions.sort(
            key=lambda a: getattr(a, "priority", 100)
        )

    def clear(self):
        self.actions.clear()

    def run(self, context):
        results = []

        for action in self.actions:

            context.log(f"Running {action.name}")

            try:

                result = action.execute(context)

                context.add_result(result)
                results.append(result)

            except Exception as e:

                context.log(f"ERROR: {e}")

                return {
                    "success": False,
                    "results": results,
                    "error": str(e)
                }

        return {
            "success": True,
            "results": results
        }
