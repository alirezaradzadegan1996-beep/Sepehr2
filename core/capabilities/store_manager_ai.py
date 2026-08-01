
from core.capabilities.base.capability import Capability


class StoreManagerAiCapability(Capability):

    name = "store_manager_ai"

    purpose = "manage store applications"
    keywords = [
        "store",
        "shop",
        "فروشگاه",
        "انبار",
        "محصول",
        "حسابداری",
        "فروش"
    ]


    def can_handle(self,text):

        return "store_manager_ai" in text



    def handle(self,text):

        return {
            "capability":"store_manager_ai",
            "status":"active",
            "version":self.version
        }



capability = StoreManagerAiCapability()
