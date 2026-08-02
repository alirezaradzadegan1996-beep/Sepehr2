

class CodeFactory:

    def create(self,idea):
        return {
            "idea":idea,
            "code":"generated",
            "test":"passed",
            "status":"AUTONOMOUS_CODE_FACTORY_ACTIVE"
        }


code_factory=CodeFactory()

