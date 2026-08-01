
from core.projects.domain_knowledge import domain_knowledge


class ProjectIntentAnalyzer:


    def analyze(self,request):

        project_type,features = domain_knowledge.detect(
            request.lower()
        )


        return {

            "request":request,

            "project_type":project_type,

            "features":features,

            "status":"understood"

        }



intent_analyzer=ProjectIntentAnalyzer()
