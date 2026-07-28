from core.capabilities import registry


class Router:

    def route(self, text):

        for capability in registry.list():

            obj = registry.get(capability)

            if hasattr(obj, "can_handle"):

                if obj.can_handle(text):

                    return obj.handle(text)

        return "فعلاً قابلیتی برای این درخواست وجود ندارد."


router = Router()
