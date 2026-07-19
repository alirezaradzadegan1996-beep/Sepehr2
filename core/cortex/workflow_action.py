from abc import ABC, abstractmethod


class WorkflowAction(ABC):

    name = "action"
    priority = 100

    @abstractmethod
    def execute(self, context):
        pass
