
import time


class RuntimeLoop:

    def __init__(self):
        self.running = False


    def start(self, cycles=1):

        self.running = True

        results = []

        for i in range(cycles):

            results.append({
                "cycle": i + 1,
                "status": "running"
            })

        return {
            "cycles": results,
            "status": "completed"
        }


runtime_loop = RuntimeLoop()
