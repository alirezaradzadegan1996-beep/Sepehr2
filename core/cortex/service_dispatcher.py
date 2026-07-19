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


        # -------------------------
        # Service Alias
        # -------------------------

        aliases = {
            "ChatService": "router",
            "MemoryService": "memory",
            "KnowledgeService": "knowledge",
            "ReasoningService": "reasoning",
            "SearchService": "search",
            "PlannerService": "planner",
            "ContextService": "context",
            "EventService": "events",
            "HealthService": "health",
        }

        service_name = aliases.get(
            service_name,
            service_name,
        )

        # -------------------------
        # Direct service lookup
        # -------------------------

        if self.cortex.has(service_name):

            service = self.cortex.get(service_name)

            if hasattr(service, "handle"):
                return service.handle(text)

            if hasattr(service, "execute"):
                return service.execute(text)

            if callable(service):
                return service(text)

            return service



        # -------------------------
        # Fallback normalized name
        # -------------------------

        registry_name = (
            service_name
            .replace("Service", "")
            .lower()
        )


        if self.cortex.has(registry_name):

            service = self.cortex.get(registry_name)

            if hasattr(service, "handle"):
                return service.handle(text)

            if hasattr(service, "execute"):
                return service.execute(text)

            if callable(service):
                return service(text)

            return service



        return (
            f"❌ Service '{service_name}' ثبت نشده است."
        )
