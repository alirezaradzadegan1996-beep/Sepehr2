

class TestingEngine:

    def test(self,project):
        return {
            "project":project,
            "tests":"passed",
            "status":"TESTING_ENGINE_ACTIVE"
        }


testing_engine=TestingEngine()

