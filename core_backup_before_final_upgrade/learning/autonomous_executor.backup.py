from core.learning.priority_engine import learning_priority
from core.learning.executor import learning_executor


class AutonomousExecutor:


    def run_once(self):

        task = learning_priority.next()


        if task is None:

            return {
                "status": "no_learning_task"
            }


        result = learning_executor.execute(task)


        return {

            "task": task,

            "result": result

        }



autonomous_executor = AutonomousExecutor()
