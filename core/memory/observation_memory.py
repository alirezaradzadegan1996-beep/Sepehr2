import json
import os
from datetime import datetime


FILE = "data/observations.json"


class ObservationMemory:


    def __init__(self):

        self.data = []

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



    def store(self, observation):

        record = {

            "time": str(datetime.now()),

            "observation": observation

        }


        self.data.append(record)

        self.save()

        return record



    def recall(self):

        return self.data



observation_memory = ObservationMemory()
