
import os

class TemplateValidator:

    def validate(self,path):
        required=[
            "main.py.template",
            "database.py.template",
            "test.py.template"
        ]

        ok=all(
            os.path.exists(
                os.path.join(path,x)
            )
            for x in required
        )

        return {
            "valid":ok,
            "path":path
        }


template_validator=TemplateValidator()
