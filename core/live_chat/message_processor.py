
class MessageProcessor:

    def process(self,message):
        return {
            "message":"processed",
            "status":"REAL_MESSAGE_PROCESSOR_ACTIVE"
        }

message_processor=MessageProcessor()
