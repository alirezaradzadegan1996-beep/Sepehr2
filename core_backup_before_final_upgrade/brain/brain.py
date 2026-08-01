from core.brain.self_evaluator import self_evaluator
from core.memory.memory_core import memory_core


class Brain:


    def process(self, text, action):

        result = action


        evaluation = self_evaluator.evaluate(
            text,
            result
        )


        memory_core.remember(
            {
                "input": text,
                "result": result,
                "evaluation": evaluation
            }
        )


        return result



brain = Brain()
