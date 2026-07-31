from datetime import datetime
import json
import os


class AdvancedMemory:


    def __init__(self):

        self.file = "data/advanced_memory.json"

        self.short_term = []
        self.long_term = []
        self.important = []


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
                    {
                        "short_term":[],
                        "long_term":[],
                        "important":[]
                    },
                    f,
                    ensure_ascii=False,
                    indent=2
                )


    def remember(self, text, importance=False):

        memory = {
            "time":str(datetime.now()),
            "text":text
        }


        self.short_term.append(memory)


        if importance:

            self.long_term.append(memory)
            self.important.append(memory)


        self.save()


        return {
            "stored":True,
            "importance":importance,
            "short_term":len(self.short_term),
            "long_term":len(self.long_term)
        }



    def save(self):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                {
                    "short_term":self.short_term,
                    "long_term":self.long_term,
                    "important":self.important
                },
                f,
                ensure_ascii=False,
                indent=2
            )


    def status(self):

        return {
            "short_term":len(self.short_term),
            "long_term":len(self.long_term),
            "important":len(self.important),
            "status":"active"
        }



memory = AdvancedMemory()


print(
    memory.remember(
        "Alireza is building Sepehr AI",
        True
    )
)


print(
    memory.status()
)


print(
    {
        "status":"advanced_memory_active",
        "time":str(datetime.now())
    }
)

