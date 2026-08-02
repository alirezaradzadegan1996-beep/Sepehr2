import json
import os


class ConceptKnowledge:

    def __init__(self):
        self.path = "data/concepts.json"


    def get(self, name):

        if not os.path.exists(self.path):
            return None

        with open(self.path, encoding="utf-8") as f:
            data = json.load(f)

        return data.get(name)


concept_knowledge = ConceptKnowledge()
