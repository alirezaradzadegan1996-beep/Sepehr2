from core.cortex.workflow_context import WorkflowContext
from core.cortex.workflow_runner import WorkflowRunner
from core.cortex.workflow_action import WorkflowAction


class TestAction(WorkflowAction):

    name = "test_action"
    priority = 1

    def execute(self, context):
        context.set("status", "ok")
        return "Action اجرا شد."


class FakeDecision:
    decision_type = "test"


class FakeDecisionResult:
    decision = FakeDecision()


ctx = WorkflowContext(
    text="سلام سپهر",
    decision=FakeDecision()
)

runner = WorkflowRunner()
runner.add(TestAction())

results = runner.run(ctx)

print("Results:", results)
print("Context:", ctx.export())
