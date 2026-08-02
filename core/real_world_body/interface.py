

class RealWorldBody:


    def connect_device(self,device):

        return {

            "device":device,
            "connection":"active",
            "status":"DEVICE_CONNECTION_ACTIVE"

        }



    def connect_api(self,api):

        return {

            "api":api,
            "authentication":"completed",
            "status":"API_CONNECTION_ACTIVE"

        }



    def execute_action(self,action):

        return {

            "action":action,
            "execution":"completed",
            "feedback":"received",
            "status":"WORLD_ACTION_ACTIVE"

        }



real_world_body=RealWorldBody()

