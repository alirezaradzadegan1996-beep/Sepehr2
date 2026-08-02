

class DeliveryBuilder:

    def deliver(self,project):
        return {
            "project":project,
            "delivery":"completed",
            "status":"FULL_DELIVERY_BUILDER_CORE_ACTIVE"
        }


delivery_builder=DeliveryBuilder()

