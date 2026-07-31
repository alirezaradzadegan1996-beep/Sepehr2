import json
import os
from datetime import datetime


class KnowledgeBrain:


    def __init__(self):

        self.file = "data/knowledge_brain.json"

        os.makedirs(
            "data",
            exist_ok=True
        )

        if not os.path.exists(self.file):

            with open(
                self.file,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    {},
                    f,
                    ensure_ascii=False
                )


    def add_knowledge(self, topic, info):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        data[topic] = info


        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=2
            )


        return {
            "status":"knowledge_added",
            "topic":topic
        }



    def search(self, topic):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            data=json.load(f)


        return {
            "topic":topic,
            "result":data.get(
                topic,
                "unknown"
            ),
            "status":"retrieved"
        }




    def query(self, topic):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        result = data.get(
            topic,
            None
        )


        if result:

            return {
                "topic":topic,
                "answer":result,
                "source":"knowledge_brain",
                "status":"found"
            }


        return {
            "topic":topic,
            "answer":None,
            "source":"knowledge_brain",
            "status":"not_found"
        }



    def learn(self, topic, information):

        self.add_knowledge(
            topic,
            information
        )


        return {
            "topic":topic,
            "saved":True,
            "status":"learned"
        }



brain = KnowledgeBrain()


print(
    brain.add_knowledge(
        "AI",
        "Artificial Intelligence studies intelligent systems"
    )
)


print(
    brain.search(
        "AI"
    )
)


print(
    {
        "status":"knowledge_brain_active",
        "time":str(datetime.now())
    }
)