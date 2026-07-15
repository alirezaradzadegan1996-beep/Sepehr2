import os


class TemplateEngine:


    def __init__(self):

        self.base_path = "core/templates"


    def get_template_path(self, project_type):

        path = os.path.join(
            self.base_path,
            project_type
        )

        if os.path.exists(path):

            return path


        return os.path.join(
            self.base_path,
            "general_app"
        )



    def get_files(self, project_type):

        path = self.get_template_path(project_type)

        files = []


        if os.path.exists(path):

            for file in os.listdir(path):

                if file.endswith(".tpl"):

                    files.append(
                        file.replace(".tpl", "")
                    )


        return files



    def exists(self, project_type):

        path = os.path.join(
            self.base_path,
            project_type
        )

        return os.path.exists(path)



    def get_template(self, project_type):

        return {
            "type": project_type,
            "path": self.get_template_path(project_type),
            "files": self.get_files(project_type)
        }
