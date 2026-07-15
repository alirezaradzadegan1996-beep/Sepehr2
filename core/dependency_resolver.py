import re


class DependencyResolver:


    def __init__(self):
        pass



    def analyze_code(self, code):

        dependencies = []

        if not code:
            return dependencies


        # from module import Class
        from_imports = re.findall(
            r"from\s+([a-zA-Z0-9_]+)\s+import",
            code
        )


        for module in from_imports:

            filename = module + ".py"

            if filename not in dependencies:
                dependencies.append(
                    filename
                )


        # import module
        imports = re.findall(
            r"^import\s+([a-zA-Z0-9_]+)",
            code,
            re.MULTILINE
        )


        for module in imports:

            filename = module + ".py"

            if filename not in dependencies:
                dependencies.append(
                    filename
                )


        return dependencies



    def resolve_project(self, files_code):

        required = []


        for filename, code in files_code.items():

            deps = self.analyze_code(
                code
            )


            for dep in deps:

                if dep not in files_code and dep not in required:
                    required.append(dep)


        return required
