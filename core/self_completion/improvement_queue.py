import json


FILE="data/self_completion/improvement_queue.json"


class ImprovementQueue:


    def add(self,item):

        try:

            with open(
                FILE,
                encoding="utf-8"
            ) as f:

                data=json.load(f)

        except:

            data=[]


        data.append(item)


        with open(
            FILE,
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
            "status":"queued",
            "item":item
        }




    def build(self, gaps):

        queue = []

        for gap in gaps.get("missing", []):

            item = {
                "type": "missing_module",
                "target": gap,
                "priority": "high"
            }

            self.add(item)
            queue.append(item)

        return queue

    def get(self):

        try:

            with open(
                FILE,
                encoding="utf-8"
            ) as f:

                return json.load(f)

        except:

            return []


improvement_queue=ImprovementQueue()
