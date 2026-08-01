
class RuntimeDispatcher:

    def __init__(self):
        self.targets = {}

    def register(self, name, target):
        self.targets[name] = target

    def dispatch(self, route, text):

        target = self.targets.get(route)

        if not target:
            return {
                "status":"failed",
                "error":f"route {route} not connected"
            }

        if hasattr(target,"handle"):
            return target.handle(text)

        if hasattr(target,"execute"):
            return target.execute(text)

        if callable(target):
            return target(text)

        return {
            "status":"failed",
            "error":"invalid target"
        }


dispatcher = RuntimeDispatcher()
