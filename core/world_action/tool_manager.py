

class ToolManager:


    def select(self, task):

        return {

            "task":
                task,

            "tool":
                "selected",

            "status":
                "TOOL_MANAGER_ACTIVE"

        }



tool_manager = ToolManager()

