from core.capabilities import registry
from core.decision.engine import decision_engine


class Router:


    def route(self, text):

        decision = decision_engine.decide(text)


        if not decision:

            return "فعلاً قابلیتی برای این درخواست وجود ندارد."


        name = decision["capability"]


        capability = registry.get(name)


        if capability and hasattr(capability, "handle"):

            return capability.handle(text)


        return "اجرای قابلیت ناموفق بود."


router = Router()
