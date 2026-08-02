
from core.builder.full_builder_engine import builder


class SelfExecutorEngine:


    def execute(self, task):

        target = task.get("target")

        request = f"create {target} module"


        result = builder.build(request)


        return {

            "target": target,

            "status": "executed",

            "builder_result": result

        }



self_executor_engine = SelfExecutorEngine()

