import json
import os


FILE = "data/self_map.json"


class SelfMap:


    def __init__(self):

        self.data = {

            "abilities": {},

            "learning": {},

            "completed": []

        }

        self.load()



    def load(self):

        if os.path.exists(FILE):

            with open(
                FILE,
                encoding="utf-8"
            ) as f:

                self.data = json.load(f)



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



    def add_ability(self,name):

        self.data["abilities"][name]="active"

        self.save()


    def complete_learning(self,name):

        self.data["learning"][name] = "completed"

        if name not in self.data["completed"]:
            self.data["completed"].append(name)

        self.save()

    def status(self):

        return self.data



self_map = SelfMap()
