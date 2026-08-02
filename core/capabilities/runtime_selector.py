
class RuntimeSelector:

    def select(self, request):

        return {
            "request": request,
            "capability": "general_capability",
            "status": "selected"
        }


runtime_selector = RuntimeSelector()
