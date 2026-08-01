from datetime import datetime


class ReflectionEngine:


    def reflect(self, experiences):

        if not experiences:

            return {
                "status":"no_experience"
            }


        success = 0
        failed = 0
        lessons = []


        for item in experiences:

            result = str(
                item.get("result","")
            ).lower()


            if "success" in result or "successfully" in result:

                success += 1


            if "fail" in result or "error" in result:

                failed += 1


            if item.get("lesson"):

                lessons.append(
                    item["lesson"]
                )


        total = success + failed


        confidence = 0

        if total:

            confidence = round(
                success / total,
                2
            )


        return {

            "status":"reflection_complete",

            "summary":{

                "successful":success,

                "failed":failed,

                "confidence":confidence

            },

            "lessons":lessons,

            "time":str(datetime.now())

        }



reflection_engine = ReflectionEngine()
