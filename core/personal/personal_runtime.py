
from core.personal.personal_ai_core import personal_ai_core


class PersonalRuntime:

    def run(self, request):

        return personal_ai_core.process(
            request
        )


personal_runtime = PersonalRuntime()
