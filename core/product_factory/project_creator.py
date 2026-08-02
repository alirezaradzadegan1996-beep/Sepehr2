

class ProjectCreator:

    def create(self,code):
        return {
            "code":code,
            "project":"created",
            "status":"PROJECT_CREATION_CORE_ACTIVE"
        }


project_creator=ProjectCreator()

