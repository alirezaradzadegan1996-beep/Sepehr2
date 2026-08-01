from core.memory.memory_core import memory_core


class LearningEngine:


    def analyze_result(self, task, result):

        lesson = {

            "task": task,

            "result": result,

            "improvement":
            "analyze future performance"

        }


        memory_core.learn(lesson)

        return lesson



learning_engine = LearningEngine()
