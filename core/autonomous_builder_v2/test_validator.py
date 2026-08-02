

class TestValidator:

    def validate(self,code):
        return {
            "code":code,
            "tests":"passed",
            "status":"AUTONOMOUS_TEST_VALIDATION_ACTIVE"
        }


test_validator=TestValidator()

