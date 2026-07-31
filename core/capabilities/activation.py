from core.capabilities.loader import discover
from core.capabilities import registry


class CapabilityActivator:


    def activate(self, name):


        loaded = discover()


        if name not in loaded:

            return {

                "status":"failed",

                "reason":"not_loaded"

            }


        capability = registry.get(
            name
        )


        if capability and hasattr(
            capability,
            "activate"
        ):

            result = capability.activate()


        else:

            result = {
                "capability":name,
                "status":"active"
            }


        return {

            "status":"activated",

            "capability":name,

            "result":result,

            "loaded":loaded

        }



capability_activator = CapabilityActivator()
