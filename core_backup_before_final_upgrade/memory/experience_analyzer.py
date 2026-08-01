from core.memory.experience_memory import experience_memory


class ExperienceAnalyzer:


    def analyze(self, skill=None):


        data = experience_memory.recall()


        results = []


        for item in data:


            if skill:

                if item.get("skill") != skill:
                    continue


            results.append(
                {
                    "skill": item.get("skill"),
                    "result": item.get("result"),
                    "lesson": item.get("lesson")
                }
            )


        return {

            "count": len(results),

            "experiences": results

        }



experience_analyzer = ExperienceAnalyzer()
