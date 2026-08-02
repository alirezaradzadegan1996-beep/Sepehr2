
class SystemAnalyzer:

    def analyze(self, system):

        return {
            "system": system,
            "needs_upgrade": True,
            "status": "analyzed"
        }


system_analyzer = SystemAnalyzer()
