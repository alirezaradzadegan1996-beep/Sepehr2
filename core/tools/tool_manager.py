

class ToolManager:

    def __init__(self):
        self.tools={}


    def register(self,name,tool):
        self.tools[name]=tool

        return {
            "tool":name,
            "status":"TOOL_REGISTERED"
        }


    def execute(self,name,data):

        return {
            "tool":name,
            "input":data,
            "status":"TOOL_EXECUTION_ACTIVE"
        }



tool_manager=ToolManager()

