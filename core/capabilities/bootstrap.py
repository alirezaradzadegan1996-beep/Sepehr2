from core.capabilities import registry
from core.services import registry as service_registry


def load_capabilities():

    if service_registry.has("memory"):
        registry.register(
            "memory",
            service_registry.get("memory")
        )

    if service_registry.has("android"):
        registry.register(
            "android",
            service_registry.get("android")
        )


load_capabilities()
