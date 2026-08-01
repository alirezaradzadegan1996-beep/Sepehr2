from datetime import datetime


class AlwaysOnRuntime:


    def __init__(self):

        self.status = "initialized"
        self.cycle_count = 0
        self.running = False



    def start(self):

        self.running = True
        self.status = "active"

        return {
            "runtime":"started",
            "status":self.status
        }



    def execute_cycle(self, input_text):

        if not self.running:

            return {
                "status":"runtime_off"
            }


        self.cycle_count += 1


        return {
            "input":input_text,
            "cycle":[
                "observe",
                "understand",
                "think",
                "act",
                "learn"
            ],
            "cycle_count":self.cycle_count,
            "status":"completed"
        }



    def health(self):

        return {
            "runtime":self.status,
            "cycles":self.cycle_count,
            "assistant":"Sepehr",
            "status":"ready"
        }



runtime = AlwaysOnRuntime()


print(
    runtime.start()
)


print(
    runtime.execute_cycle(
        "سلام سپهر"
    )
)


print(
    runtime.health()
)


print(
    {
        "status":"always_on_runtime_active",
        "time":str(datetime.now())
    }
)

