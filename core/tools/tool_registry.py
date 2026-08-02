
class ToolRegistry:

    def __init__(self):
        self.tools = {}


    def register(self, name, tool):

        self.tools[name] = tool

        return {
            "tool": name,
            "status": "registered"
        }


    def get(self, name):

        return self.tools.get(name)


tool_registry = ToolRegistry()
