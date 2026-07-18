"""
Sepehr2 Cortex
مرکز مدیریت تمام سرویس‌های سیستم
"""

from .registry import registry
from .engine import CortexEngine
from .skill_manager import SkillManager


class Cortex:

    def __init__(self):

        self.registry = registry

        self.engine = CortexEngine(self.registry)

        from .action_chain import ActionChain

        self.engine.action_chain = ActionChain(self)

        self.skill_manager = SkillManager()


    # -------------------------
    # Service Registry
    # -------------------------

    def register(self, name, service):

        self.registry.register(
            name,
            service
        )


    def register_safe(self, name, service):

        return self.registry.register_safe(
            name,
            service
        )


    def unregister(self, name):

        self.registry.unregister(name)


    def has(self, name):

        return self.registry.has(name)


    def get(self, name):

        return self.registry.get(name)



    # -------------------------
    # Service Execution
    # -------------------------

    def execute(self, name, *args, **kwargs):

        return self.engine.execute(
            name,
            *args,
            **kwargs
        )



    # -------------------------
    # Decision Engine
    # -------------------------

    def decide(self, text):
        return self.engine.decide(text)

    def services(self):

        return self.registry.list()



    # -------------------------
    # Skill Management
    # -------------------------

    def set_skills(self, skills):

        self.skill_manager = SkillManager(
            skills
        )


    def load_skills(self):
        """
        Load all available skills into Cortex SkillManager.
        """

        from core.skill_registry import get_skills

        skills = get_skills()

        self.skill_manager = SkillManager(
            skills=skills
        )

        return skills


    def get_skills(self):

        return self.skill_manager.skills



    def find_skill(self, text, intent=None):

        return self.skill_manager.find(
            text,
            intent
        )



    def skills(self):

        return self.skill_manager.list()



    # -------------------------
    # System Status
    # -------------------------

    def status(self):

        return {

            "services": self.registry.list(),

            "engine": self.engine.report(),

            "skills": self.skill_manager.list()

        }



    # -------------------------
    # Health Check
    # -------------------------

    def health(self):

        result = {}

        for service in self.registry.list():

            obj = self.registry.get(service)

            result[service] = {

                "status": "ok",

                "type": type(obj).__name__

            }


        return result



cortex = Cortex()
