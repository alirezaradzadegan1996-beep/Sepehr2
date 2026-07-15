from pathlib import Path

from core.template_loader import TemplateLoader
from core.template_renderer import TemplateRenderer
from core.template_selector import TemplateSelector
from core.code_evolution import CodeEvolution
from core.dependency_resolver import DependencyResolver


class CodeEngine:

    def __init__(self):
        self.loader = TemplateLoader()
        self.renderer = TemplateRenderer()
        self.selector = TemplateSelector()
        self.evolution = CodeEvolution()
        self.dependency = DependencyResolver()


    def generate(self, project_path, analysis):

        project_type = analysis.get(
            "type",
            "general"
        )

        files = self.get_files(project_type)


        # اضافه کردن تجربه پروژه‌های قبلی
        evolution_result = self.evolution.apply(
            project_type,
            files
        )

        files = evolution_result.get(
            "files",
            files
        )


        output = Path(project_path)

        output.mkdir(
            parents=True,
            exist_ok=True
        )


        generated = []


        # مرحله اول تولید فایل‌ها
        for filename in files:

            template = self.loader.load(
                project_type,
                filename
            )

            if not template:
                continue


            context = {
                "project_name": analysis.get(
                    "goal",
                    project_type
                ),

                "learned_features": ", ".join(
                    analysis.get(
                        "learned_features",
                        []
                    )
                ),

                "experience_used": str(
                    evolution_result.get(
                        "evolution",
                        {}
                    ).get(
                        "experience_used",
                        False
                    )
                )
            }


            code = self.renderer.render(
                template,
                context
            )


            file_path = output / filename

            file_path.write_text(
                code,
                encoding="utf-8"
            )


            generated.append(filename)



        # مرحله دوم: کشف وابستگی‌ها
        dependencies = []


        for filename in generated:

            file_path = output / filename

            code = file_path.read_text(
                encoding="utf-8"
            )


            deps = self.dependency.analyze_code(
                code
            )


            for dep in deps:

                if dep not in dependencies:
                    dependencies.append(dep)



        # تولید فایل‌های وابسته
        for dep in dependencies:

            if dep in generated:
                continue


            template = self.loader.load(
                project_type,
                dep
            )


            if template:

                code = self.renderer.render(
                    template,
                    {}
                )


                (output / dep).write_text(
                    code,
                    encoding="utf-8"
                )


                generated.append(dep)



        return (
            "💻 کدهای پروژه تولید شدند.\n\n"
            f"نوع پروژه: {project_type}\n"
            f"فایل‌ها: {len(generated)} عدد\n\n"
            +
            "\n".join(generated)
        )



    def get_files(self, project_type):

        if project_type == "calculator":

            return [
                "main.py",
                "calculator.py",
                "test.py"
            ]


        if project_type == "ecommerce":

            return [
                "main.py",
                "product.py",
                "cart.py",
                "database.py",
                "user.py",
                "test.py"
            ]


        return [
            "main.py",
            "test.py"
        ]
