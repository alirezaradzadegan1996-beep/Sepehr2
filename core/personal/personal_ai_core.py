
from core.personal.personality_core import personality_core
from core.personal.user_context import user_context


class PersonalAICore:

    def process(self, request):

        personality = personality_core.get()

        context = user_context.load()

        return {
            "request": request,
            "personality": personality,
            "context": context,
            "response": "generated",
            "status": "SEPEHR_PERSONAL_AI_ACTIVE"
        }


personal_ai_core = PersonalAICore()
