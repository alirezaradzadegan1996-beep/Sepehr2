

class CapabilityAnalyzer:


    def analyze(self, capabilities):

        weak=[]

        for name,score in capabilities.items():

            if score < 80:
                weak.append(name)


        return {
            "weak_points": weak,
            "analysis":"completed",
            "status":"CAPABILITY_ANALYSIS_ACTIVE"
        }



capability_analyzer = CapabilityAnalyzer()

