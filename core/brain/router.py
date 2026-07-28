from core.services import registry

class Router:

    def route(self, text):

        for service in registry.list():

            obj = registry.get(service)

            if hasattr(obj, "can_handle"):

                if obj.can_handle(text):

                    return obj.handle(text)

        return "فعلاً سرویسی برای این درخواست وجود ندارد."

router = Router()
