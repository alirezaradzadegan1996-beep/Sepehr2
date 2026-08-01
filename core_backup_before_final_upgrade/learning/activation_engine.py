from core.capabilities.loader import discover
from core.capabilities import registry


class ActivationEngine:


    def activate(self, name):


        loaded = discover()


        if name in registry.list():

            return {

                "status": "activated",

                "capability": name,

                "loaded": loaded

            }


        return {

            "status": "failed",

            "capability": name,

            "loaded": loaded

        }



activation_engine = ActivationEngine()
