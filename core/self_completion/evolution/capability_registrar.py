
from core.capabilities.registry import registry


class CapabilityRegistrar:


    def register(self, name):

        existing = registry.list()

        if name in existing:

            return {
                "status":"exists",
                "capability":name
            }


        registry.register(
            name,
            None
        )

        registry.save()


        return {
            "status":"registered",
            "capability":name
        }



capability_registrar = CapabilityRegistrar()

