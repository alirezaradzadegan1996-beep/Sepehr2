from .workflow_context import WorkflowContext
from .workflow_runner import WorkflowRunner
from .service_action import ServiceAction


class ActionChain:
    """
    اجرای Workflow سرویس‌های Cortex
    """

    def __init__(self, cortex):
        self.cortex = cortex

    def run(self, service, method=None, *args, **kwargs):

        text = ""

        if args:
            text = args[0]

        class FakeDecision:
            decision_type = "workflow"

        context = WorkflowContext(
            text=text,
            decision=FakeDecision(),
        )

        runner = WorkflowRunner()

        runner.add(
            ServiceAction(
                service,
                method,
                *args,
                **kwargs,
            )
        )

        result = runner.run(context)

        if result["results"]:
            return result["results"][-1]

        return None
