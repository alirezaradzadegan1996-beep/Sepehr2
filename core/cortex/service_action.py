from core.cortex.workflow_action import WorkflowAction


class ServiceAction(WorkflowAction):

    name = "service"
    priority = 10

    def __init__(self, service, method=None, *args, **kwargs):
        self.service = service
        self.method = method
        self.args = args
        self.kwargs = kwargs

    def execute(self, context):

        if self.method:

            func = getattr(self.service, self.method)

            return func(
                *self.args,
                **self.kwargs
            )

        if hasattr(self.service, "handle"):
            return self.service.handle(context.text)

        if hasattr(self.service, "execute"):
            return self.service.execute(context.text)

        if callable(self.service):
            return self.service(context.text)

        return self.service
