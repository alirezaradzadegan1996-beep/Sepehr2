from core.learning.priority_engine import learning_priority
from core.learning.executor import learning_executor
from core.learning.activation_engine import activation_engine
from core.learning.state_manager import state_manager


class AutonomousExecutor:


    def run(self, skill):

        task = {
            "skill": skill,
            "priority": 10,
            "status": "waiting"
        }

        return self._execute(task)



    def run_once(self):

        task = learning_priority.next()

        if task is None:

            return {
                "status":"no_learning_task"
            }

        return self._execute(task)



    def _execute(self, task):

        result = learning_executor.execute(task)

        activation = None


        if "creation" in result:

            creation = result["creation"]

            if (
                creation.get("test",{}).get("valid")
                or creation.get("status") == "exists"
            ):

                activation = activation_engine.activate(
                    task["skill"]
                )


        state = None


        if activation and activation.get("status") == "activated":

            state = state_manager.complete(
                task["skill"]
            )


        return {

            "task": task,

            "result": result,

            "activation": activation,

            "state": state

        }



autonomous_executor = AutonomousExecutor()
