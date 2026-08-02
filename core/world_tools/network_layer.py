

class NetworkLayer:

    def connect(self,target):
        return {
            "target":target,
            "connection":"active",
            "status":"NETWORK_COMMUNICATION_ACTIVE"
        }


network_layer=NetworkLayer()

