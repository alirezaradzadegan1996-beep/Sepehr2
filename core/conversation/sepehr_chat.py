from datetime import datetime


class ConversationMemory:

    def __init__(self):
        self.history=[]


    def add(self,message):

        self.history.append({
            "time":str(datetime.now()),
            "message":message
        })

        return {
            "stored":True,
            "count":len(self.history)
        }



class SepehrPersonality:

    def profile(self):

        return {
            "name":"Sepehr",
            "style":"friendly",
            "identity":"digital_agent"
        }



class ConversationEngine:

    def __init__(self):

        self.memory = ConversationMemory()
        self.personality = SepehrPersonality()


    def talk(self,message):

        self.memory.add(message)

        return {
            "input":message,
            "context":"loaded",
            "personality":self.personality.profile(),
            "response":"message understood",
            "status":"ready"
        }



chat = ConversationEngine()


print(
    chat.talk(
        "سلام سپهر"
    )
)

