
class FeatureBrain:

    def extract(self,project):

        return {
            "core_features":project.get("features",[]),
            "generated":True
        }


feature_brain=FeatureBrain()
