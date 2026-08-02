

class ProjectAnalyzer:

    def analyze(self,idea):
        return {
            "idea":idea,
            "requirements":"identified",
            "status":"PROJECT_ANALYSIS_ACTIVE"
        }


project_analyzer=ProjectAnalyzer()

