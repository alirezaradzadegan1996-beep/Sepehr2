

class CodeGenerator:

    def generate(self,design):
        return {
            "design":design,
            "code":"generated",
            "status":"CODE_GENERATION_ACTIVE"
        }


code_generator=CodeGenerator()

