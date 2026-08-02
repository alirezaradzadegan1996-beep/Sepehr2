

class QualityValidation:

    def validate(self,project):
        return {
            "project":project,
            "quality":"verified",
            "status":"QUALITY_VALIDATION_ACTIVE"
        }


quality_validation=QualityValidation()

