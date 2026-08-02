

class DeliveryCore:

    def deliver(self,product):
        return {
            "product":product,
            "delivery":"completed",
            "status":"PRODUCT_DELIVERY_CORE_ACTIVE"
        }


delivery_core=DeliveryCore()

