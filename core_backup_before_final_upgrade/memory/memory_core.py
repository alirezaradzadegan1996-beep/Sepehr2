import json
import os


class MemoryCore:

    def __init__(self):

        self.experience_file = "data/experiences.json"
        self.lesson_file = "data/lessons.json"


    def _load(self, file):

        if not os.path.exists(file):
            return []

        with open(file,"r",encoding="utf-8") as f:
            return json.load(f)



    def _save(self,file,data):

        with open(file,"w",encoding="utf-8") as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=2
            )



    def remember(self, experience):

        data = self._load(self.experience_file)

        data.append(experience)

        self._save(
            self.experience_file,
            data
        )

        return True



    def learn(self, lesson):

        data = self._load(self.lesson_file)

        data.append(lesson)

        self._save(
            self.lesson_file,
            data
        )

        return True



    def recall(self):

        return self._load(
            self.experience_file
        )



memory_core = MemoryCore()
