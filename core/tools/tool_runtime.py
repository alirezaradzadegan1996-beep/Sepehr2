
from core.tools.tool_registry import tool_registry
from core.tools.file_tool import file_tool
from core.tools.code_tool import code_tool


class ToolRuntime:

    def __init__(self):

        tool_registry.register(
            "file",
            file_tool
        )

        tool_registry.register(
            "code",
            code_tool
        )


    def run(self, name, data):

        tool = tool_registry.get(
            name
        )

        if tool:

            return tool.execute(
                data
            )

        return {
            "status":"tool_not_found"
        }


tool_runtime = ToolRuntime()
