
import os

class SkillRegistry:

    def __init__(self):
        self.skills={}

    def register(self,name,skill):
        self.skills[name]=skill
        return {"status":"registered","skill":name}

    def get(self,name):
        return self.skills.get(name)

    def all(self):
        return list(self.skills.keys())

skill_registry=SkillRegistry()
