import json
import os
from datetime import datetime


FILE = "data/experiences.json"


class ExperienceMemory:


    def __init__(self):

        self.load()



    def load(self):

        if os.path.exists(FILE):

            with open(
                FILE,
                encoding="utf-8"
            ) as f:

                self.data = json.load(f)

        else:

            self.data = []



    def save(self):

        with open(
            FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.data,
                f,
                ensure_ascii=False,
                indent=2
            )



    def remember(
        self,
        goal,
        skill,
        result,
        lesson
    ):

        item = {

            "time":str(datetime.now()),

            "goal":goal,

            "skill":skill,

            "result":result,

            "lesson":lesson

        }


        self.data.append(item)

        self.save()


        return item



    def recall(self):

        return self.data



experience_memory = ExperienceMemory()
