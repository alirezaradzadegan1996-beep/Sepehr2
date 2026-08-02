
class InputGateway:

    def receive(self,message):
        return {
            "message":message,
            "status":"LIVE_INPUT_GATEWAY_ACTIVE"
        }

input_gateway=InputGateway()
