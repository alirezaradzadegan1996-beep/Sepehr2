from core.learning.learning_engine import learning_engine
from core.learning.failure_analyzer import failure_analyzer


class SelfEvaluator:


    def evaluate(self, task, result):


        failed_messages = [

            "فعلاً قابلیتی برای این درخواست وجود ندارد",
            "Router فعال نیست",
            "خطا",
            "error"

        ]


        success = True


        if result is None:

            success = False


        if isinstance(result,str):

            for msg in failed_messages:

                if msg in result:

                    success = False



        evaluation = {

            "task": task,

            "success": success,

            "result": result

        }


        if not success:

            evaluation["weakness"] = failure_analyzer.analyze(
                task,
                result
            )


        learning_engine.analyze_result(
            task,
            evaluation
        )


        return evaluation



self_evaluator = SelfEvaluator()
