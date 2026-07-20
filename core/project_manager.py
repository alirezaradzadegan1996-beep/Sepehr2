import json
import os

from core.planner_v2 import make_plan, current_step, next_step
from core.code_engine import CodeEngine
from core.test_engine import TestEngine
from core.debug_engine import DebugEngine
from core.auto_fix_engine import AutoFixEngine
from core.app_builder import AppBuilder
from core.project_analyzer import ProjectAnalyzer
from core.project_reasoner import ProjectReasoner
from core.project_optimizer import ProjectOptimizer
from core.project_builder import ProjectBuilder
from core.project_memory import ProjectMemory
from core.project_experience import ProjectExperience
from core.experience_memory import ExperienceMemory
from core.project_learner import ProjectLearner
from core.project_learning_engine import ProjectLearningEngine
from core.knowledge_optimizer import KnowledgeOptimizer


FILE = "data/project.json"


class ProjectManager:

    def __init__(self):
        self.project_learner = ProjectLearner()
        self.builder = ProjectBuilder()
        self.project_memory = ProjectMemory()
        self.code_engine = CodeEngine()
        self.debug_engine = DebugEngine()
        self.auto_fix_engine = AutoFixEngine()
        self.analyzer = ProjectAnalyzer()
        self.optimizer = ProjectOptimizer()
        self.reasoner = ProjectReasoner()
        self.project_experience = ProjectExperience()
        self.experience_memory = ExperienceMemory()
        self.learning_engine = ProjectLearningEngine()
        self.knowledge_optimizer = KnowledgeOptimizer()

        self.active = None
        self.load()


    def save(self):
        os.makedirs("data", exist_ok=True)

        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(
                self.active,
                f,
                ensure_ascii=False,
                indent=4
            )


    def load(self):
        if os.path.exists(FILE):
            try:
                with open(FILE, "r", encoding="utf-8") as f:
                    self.active = json.load(f)
            except:
                self.active = None
        else:
            self.active = None


    def get_active(self):
        self.load()
        return self.active


    def start_project(self, task):

        self.active = make_plan(task)

        analysis = self.analyzer.analyze(task)

        reasoning = self.reasoner.analyze(task)

        learning = self.learning_engine.learn_context(
            reasoning.get(
                "type",
                "general"
            )
        )

        reasoning["learning"] = learning

        analysis["reasoning"] = reasoning

        # استفاده از تصمیم Reasoner قبل از Optimizer
        analysis["type"] = reasoning.get(
            "type",
            analysis.get("type")
        )

        analysis["files"] = reasoning.get(
            "modules",
            analysis.get("files")
        )

        analysis["features"] = reasoning.get(
            "suggestions",
            analysis.get("features")
        )

        # استفاده از دانش پروژه‌های قبلی
        analysis = self.knowledge_optimizer.optimize(
            analysis
        )

        analysis["learned_files"] = analysis.get(
            "learned_files",
            analysis.get(
                "reasoning",
                {}
            ).get(
                "experience_memory",
                {}
            ).get(
                "files",
                []
            )
        )

        # حالا Optimizer نوع صحیح را می‌بیند
        optimization = self.optimizer.optimize(analysis)

        analysis["optimization"] = optimization

        self.active["analysis"] = analysis

        project_dir = os.path.join(
            "projects",
            self.active["id"]
        )

        os.makedirs(project_dir, exist_ok=True)

        # فقط پوشه پروژه ساخته می‌شود.
        # اجرای مراحل بر عهده AppBuilder است.

        os.makedirs(project_dir, exist_ok=True)

        self.active["step"] = 0

        self.save()

        return (
            f"📌 پروژه ایجاد شد\n\n"
            f"شناسه: {self.active['id']}\n"
            f"وضعیت: {self.active['status']}\n\n"
            f"نوع پروژه:\n"
            f"{analysis['type']}\n\n"
            f"مرحله ۱:\n"
            f"{current_step(self.active)}"
        )


    def generate_code(self):

        if not self.active:
            return "❌ پروژه‌ای وجود ندارد."

        engine = CodeEngine()

        return engine.generate(self.active)


    def run_test(self):

        if not self.active:
            return "❌ پروژه‌ای وجود ندارد."

        tester = TestEngine()

        result = tester.run(
            self.active
        )

        self.active["test_result"] = result


        # چرخه تعمیر خودکار
        if isinstance(result, dict) and not result.get("success"):

            debug = self.debug_engine.analyze(
                self.active,
                result
            )


            if isinstance(debug, dict):

                filename = debug.get("file")

                analysis = self.active.get(
                    "analysis",
                    {}
                )

                project_type = analysis.get(
                    "type",
                    "general"
                )

                project_id = self.active.get(
                    "id"
                )


                if filename and project_id:

                    fix = self.auto_fix_engine.apply_fix(
                        f"projects/{project_id}",
                        project_type,
                        filename
                    )


                    if fix.get("fixed"):

                        retry = tester.run(
                            self.active
                        )

                        self.active["test_result"] = retry

                        result = {
                            "success": retry.get(
                                "success",
                                False
                            ),
                            "auto_fixed": True,
                            "fix": fix,
                            "retry": retry
                        }


        self.save()

        return result


    def debug_project(self):

        result = self.debug_engine.analyze(
            self.active,
            self.active.get("test_result")
        )

        return result.get(
            "message",
            str(result)
        )


    def continue_project(self):

        self.load()

        if not self.active:
            return "❌ هیچ پروژه فعالی وجود ندارد."


        if self.active.get("status") == "completed":
            return (
                "✅ این پروژه قبلاً تکمیل شده است.\n\n"
                f"📌 پروژه: {self.active.get('goal')}"
            )


        step = next_step(self.active)


        if step is None:

            self.active["status"] = "completed"

            self.save()

            self.project_memory.remember_project(
                self.active
            )

        # learn successful project experience
        if self.active.get("test_result"):

            self.experience_memory.learn_from_project(
                self.active
            )

            learning = self.project_learner.learn_from_project(
                self.active
            )

            self.active["learning_result"] = learning

            return (
                "🚀 پروژه کامل شد.\n\n"
                f"📌 نام پروژه:\n"
                f"{self.active.get('goal')}\n\n"
                "✅ تحویل پروژه انجام شد."
            )


        self.save()


        result = AppBuilder.run(
            self.active,
            self.active.get("step", 0)
        )

        if isinstance(result, dict):

            if result.get("status") == "ready":
                self.active["status"] = "completed"

                reasoning = self.active.get(
                    "analysis",
                    {}
                ).get(
                    "reasoning",
                    {}
                )

                experience = reasoning.get(
                    "experience",
                    {}
                )

                experience_id = experience.get(
                    "best_project_id"
                )

                test_result = self.active.get(
                    "test_result",
                    ""
                )

                success = "✅ تست موفق" in test_result

                if (
                    reasoning.get("experience_used")
                    and experience_id
                ):
                    feedback = self.project_experience.apply_feedback(
                        experience_id,
                        success
                    )

                    self.active["experience_feedback"] = feedback

                self.project_memory.remember_project(
                    self.active
                )

            self.save()

            return (
                f"📌 پروژه: {self.active.get('goal')}\n\n"
                f"{result.get('message','')}"
            )


        return result


    def next_step(self):

        return self.continue_project()


    def show_project(self):

        self.load()

        if not self.active:
            return "❌ پروژه‌ای وجود ندارد."


        return (
            f"📌 پروژه: {self.active['goal']}\n"
            f"مرحله: {self.active['step'] + 1}\n"
            f"وضعیت: {self.active['status']}"
        )


    def finish_project(self):

        if self.active:
            self.project_memory.remember(
                self.active
            )

        self.active = None

        if os.path.exists(FILE):
            os.remove(FILE)

        return "✅ پروژه حذف شد."



_pm = ProjectManager()


def start_project(task):
    return _pm.start_project(task)


def continue_project():
    return _pm.continue_project()


def show_project():
    return _pm.show_project()


def finish_project():
    return _pm.finish_project()
