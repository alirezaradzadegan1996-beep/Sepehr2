import os


# Fix Template Engine
path="core/templates/template_engine.py"

with open(path,"w",encoding="utf-8") as f:
    f.write(r'''
import os


class TemplateEngine:

    name="template_engine"


    def __init__(self):

        self.base="core/templates/generated"


        os.makedirs(
            self.base,
            exist_ok=True
        )


    def find(self,name):

        return os.path.join(
            self.base,
            name
        )


    def exists(self,name):

        return os.path.exists(
            self.find(name)
        )


    def create(self,name,features):

        path=self.find(name)

        os.makedirs(
            path,
            exist_ok=True
        )


        files={

            "main.py.template":
f'''# Generated {name}

def main():
    print("Sepehr generated {name}")


if __name__=="__main__":
    main()
''',

            "database.py.template":
'''
class Database:

    def connect(self):
        return True
''',

            "test.py.template":
'''
def test():
    return True
'''

        }


        for file,data in files.items():

            with open(
                os.path.join(path,file),
                "w",
                encoding="utf-8"
            ) as f:
                f.write(data)


        return path



    def get_or_create(self,name,features):

        if not self.exists(name):

            self.create(
                name,
                features
            )


        return name



    def load(self,name):

        path=self.find(name)

        result={}


        if not os.path.exists(path):

            return result


        for file in os.listdir(path):

            if file.endswith(".template"):

                with open(
                    os.path.join(path,file),
                    encoding="utf-8"
                ) as f:

                    result[
                        file.replace(".template","")
                    ]=f.read()


        return result



template_engine=TemplateEngine()
''')



# Fix Builder connection

path="core/builder/full_builder_engine.py"

with open(path,"r",encoding="utf-8") as f:
    data=f.read()


old='''        templates = template_engine.load(
            template
        )
'''

new='''        if isinstance(template, dict):

            template_name = intent["project_type"]

        else:

            template_name = template


        template_name = template_engine.get_or_create(
            template_name,
            intent["features"]
        )


        templates = template_engine.load(
            template_name
        )
'''


data=data.replace(
    old,
    new
)


with open(path,"w",encoding="utf-8") as f:
    f.write(data)



print("TEMPLATE SYSTEM UPGRADED")
