from datetime import datetime
import json
import os


class SelfSkillCreator:


    def __init__(self):

        self.file = "data/skills_registry.json"

        self.skills = []

        os.makedirs(
            "data",
            exist_ok=True
        )


        if os.path.exists(self.file):

            with open(
                self.file,
                "r",
                encoding="utf-8"
            ) as f:

                self.skills = json.load(f)



    def create_skill(self, name, purpose):

        skill = {
            "name": name,
            "purpose": purpose,
            "version": "1.0",
            "status": "created",
            "time": str(datetime.now())
        }


        self.skills.append(skill)

        self.save()


        return {
            "skill": name,
            "status": "created"
        }



    def save(self):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.skills,
                f,
                ensure_ascii=False,
                indent=2
            )



    def list_skills(self):

        return {
            "skills": self.skills,
            "count": len(self.skills),
            "status": "registered"
        }



creator = SelfSkillCreator()


print(
    creator.create_skill(
        "car_market_skill",
        "build and manage vehicle marketplace applications"
    )
)


print(
    creator.list_skills()
)


print(
    {
        "status":"self_skill_creator_active",
        "time":str(datetime.now())
    }
)

