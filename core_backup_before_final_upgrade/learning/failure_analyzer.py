class FailureAnalyzer:


    def analyze(self, task, result):

        weakness = "unknown"


        if isinstance(result, str):

            if "قابلیتی" in result:
                weakness = "missing_capability"


            elif "خطا" in result or "error" in result:
                weakness = "runtime_error"


            elif "Router" in result:
                weakness = "routing_problem"


        analysis = {

            "task": task,

            "result": result,

            "weakness": weakness,

            "suggestion": self.suggest(weakness)

        }


        return analysis



    def suggest(self, weakness):

        suggestions = {

            "missing_capability":
            "نیاز به توسعه Capability جدید",

            "runtime_error":
            "نیاز به بررسی و اصلاح کد",

            "routing_problem":
            "نیاز به بهبود تصمیم گیری Router",

            "unknown":
            "نیاز به تحلیل بیشتر"

        }


        return suggestions.get(
            weakness,
            "تحلیل نامشخص"
        )



failure_analyzer = FailureAnalyzer()
