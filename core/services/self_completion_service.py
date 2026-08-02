from core.self_completion import self_completion_engine


class SelfCompletionService:


    name = "self_completion"


    def analyze(self):

        return self_completion_engine.run_analysis()



self_completion_service = SelfCompletionService()
