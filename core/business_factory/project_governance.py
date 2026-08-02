

class ProjectGovernance:

    def manage(self,project):
        return {
            "project":project,
            "tasks":"controlled",
            "status":"PROJECT_GOVERNANCE_ACTIVE"
        }


project_governance=ProjectGovernance()

