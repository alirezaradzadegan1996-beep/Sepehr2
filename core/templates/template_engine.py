import os


class TemplateEngine:


    name="template_engine"


    def __init__(self):

        self.base="core/templates/generated"


    def find(self,name):

        path=os.path.join(
            self.base,
            name
        )

        if os.path.exists(path):
            return path

        return None



    def load(self,name):

        path=self.find(name)

        if not path:
            return {}


        files={}


        for file in os.listdir(path):

            if file.endswith(".template"):

                with open(
                    os.path.join(path,file),
                    encoding="utf-8"
                ) as f:

                    new_name=file.replace(
                        ".template",
                        ""
                    )

                    files[new_name]=f.read()


        return files



    def get_or_create(self,name,features):

        path=self.find(name)

        if path:
            return self.load(name)


        from core.templates.template_creator import template_creator


        result=template_creator.create(
            name,
            features
        )


        return self.load(name)



template_engine=TemplateEngine()
