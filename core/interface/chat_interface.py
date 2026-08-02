
class ChatInterface:

    def receive(self, text):

        return {
            "input": text,
            "status": "received"
        }


    def display(self, response):

        return {
            "response": response,
            "status": "displayed"
        }


chat_interface = ChatInterface()
