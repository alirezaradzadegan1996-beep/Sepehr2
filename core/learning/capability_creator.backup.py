import os


class CapabilityCreator:


    def create(self, name):

        filename = (
            f"core/capabilities/{name}.py"
        )


        if os.path.exists(filename):

            return {
                "status": "exists",
                "file": filename
            }


        template = f'''
class {name.title().replace("_","")}Capability:


    name = "{name}"


    def can_handle(self, text):

        return "{name}" in text



    def handle(self, text):

        return {{
            "capability": "{name}",
            "message": "new capability created"
        }}



capability = {name.title().replace("_","")}Capability()
'''


        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(template)



        return {

            "status": "created",

            "file": filename

        }



capability_creator = CapabilityCreator()
