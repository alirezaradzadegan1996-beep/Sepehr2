import json
import os
from datetime import datetime


class PermanentMemory:

    def __init__(self):

        self.file = "data/permanent_memory.json"

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
                    [],
                    f
                )


    def save(self, item):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            memories=json.load(f)


        memories.append(
            {
                "time":str(datetime.now()),
                "memory":item
            }
        )


        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                memories,
                f,
                ensure_ascii=False,
                indent=2
            )


        return {
            "status":"saved",
            "count":len(memories)
        }



    def recall(self):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)



memory = PermanentMemory()


print(
    memory.save(
        "completed conversation integration"
    )
)


print(
    memory.recall()
)

