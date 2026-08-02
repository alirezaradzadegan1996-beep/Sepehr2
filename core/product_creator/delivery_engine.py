

class DeliveryEngine:

    def deliver(self,product):
        return {
            "delivery":"completed",
            "deployment":"active",
            "status":"AUTONOMOUS_DELIVERY_ACTIVE"
        }


delivery_engine=DeliveryEngine()

