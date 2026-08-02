

class UIGateway:

    def connect(self,user):
        return {
            "user":user,
            "interface":"connected",
            "status":"USER_INTERFACE_GATEWAY_ACTIVE"
        }


ui_gateway=UIGateway()

