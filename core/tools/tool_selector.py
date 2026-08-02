
class ToolSelector:

    def select(self, request):

        if "file" in request:

            tool = "file"

        elif "code" in request:

            tool = "code"

        else:

            tool = "general"


        return {
            "request": request,
            "selected_tool": tool,
            "status": "selected"
        }


tool_selector = ToolSelector()
