from datetime import datetime


class ConversationIntelligence:


    def __init__(self):

        self.history = []

        self.personality = "Sepehr"



    def understand(self, text):

        if text in ["سلام", "چخبر", "خوبی؟"]:

            intent = "casual_chat"

        else:

            intent = "general_question"


        return {
            "text": text,
            "intent": intent,
            "status": "understood"
        }



    def generate_response(self, context):

        if context["intent"] == "casual_chat":

            response = "سلام علیرضا، من فعال هستم و آماده‌ام کمک کنم."

        else:

            response = "پیامت دریافت شد، در حال بررسی هستم."


        return {
            "response": response,
            "personality": self.personality,
            "status": "generated"
        }



    def remember(self, text, response):

        self.history.append(
            {
                "input": text,
                "response": response,
                "time": str(datetime.now())
            }
        )


        return {
            "memory_saved": True,
            "count": len(self.history)
        }




conversation = ConversationIntelligence()


context = conversation.understand(
    "چخبر"
)

print(context)


answer = conversation.generate_response(
    context
)

print(answer)


print(
    conversation.remember(
        "چخبر",
        answer["response"]
    )
)


print(
    {
        "status":"conversation_intelligence_active"
    }
)

