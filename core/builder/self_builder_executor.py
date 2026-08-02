
class SelfBuilderExecutor:

    def build(self, plan):

        return {
            "project": "auto_generated_module",
            "plan": plan,
            "files": [
                "main.py",
                "test.py",
                "README.md"
            ],
            "status": "created"
        }


self_builder_executor = SelfBuilderExecutor()
