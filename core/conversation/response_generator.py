
class ResponseGenerator:

    def generate(self, data):
        return {
            "response": "Sepehr ready",
            "data": data,
            "status": "generated"
        }

response_generator = ResponseGenerator()
