

class InputProcessor:


    def process(self, request):

        return {

            "request":
                request,

            "analysis":
                "completed",

            "status":
                "INPUT_PROCESSING_ACTIVE"

        }


input_processor = InputProcessor()

