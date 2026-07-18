from core.cortex.service import Service


class ServiceDispatcher(Service):
    """
    Cortex Service Dispatcher

    مسئول پیدا کردن و اجرای سرویس‌ها
    """

    name = "dispatcher"

    def __init__(self, cortex):
        self.cortex = cortex

    def dispatch(self, service_name, text):

        if not service_name:
            return None

        # ProjectService -> project
        registry_name = service_name.replace(
            "Service",
            ""
        ).lower()

        if not self.cortex.has(registry_name):

            router = self.cortex.get("router")

            if hasattr(router, "handle"):
                return router.handle(text)

            return (
                f"❌ Service '{registry_name}' ثبت نشده است."
            )

        service = self.cortex.get(registry_name)

        if hasattr(service, "handle"):
            return service.handle(text)

        if hasattr(service, "execute"):
            return service.execute(text)

        if callable(service):
            return service(text)

        return service
