
import os


class TemplateEngine:


    def load(self,result):

        files={}

        if isinstance(result,dict):

            path=result.get("path")

            if not path:

                path=f"core/templates/generated/{result.get('template')}"


        else:

            path=f"core/templates/generated/{result}"


        if not os.path.exists(path):
            return files


        for f in os.listdir(path):

            with open(
                os.path.join(path,f),
                encoding="utf-8"
            ) as x:

                files[
                    f.replace(".template","")
                ]=x.read()


        return files



template_engine=TemplateEngine()
