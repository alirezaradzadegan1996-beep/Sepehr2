from datetime import datetime


class SepehrRuntime:

    def start(self):
        return {
            "runtime": "started",
            "cortex": "connected",
            "status": "active"
        }


    def execute(self, text):
        return {
            "input": text,
            "pipeline": [
                "context",
                "reasoning",
                "decision",
                "action"
            ],
            "status": "executed"
        }


sepehr_runtime = SepehrRuntime()


print(
    sepehr_runtime.start()
)


print(
    sepehr_runtime.execute(
        "hello sepehr"
    )
)

