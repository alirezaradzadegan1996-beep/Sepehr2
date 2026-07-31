from datetime import datetime


class WorldInterface:

    def __init__(self):

        self.tools = []


    def register_tool(self, tool):

        self.tools.append(tool)

        return {
            "tool": tool,
            "status":"registered"
        }


    def connect(self):

        return {
            "connected_tools": self.tools,
            "world_interface":"active",
            "status":"connected"
        }



world = WorldInterface()


for tool in [
    "file_system",
    "web",
    "android",
    "camera",
    "voice"
]:

    print(
        world.register_tool(tool)
    )


print(
    world.connect()
)


print(
    {
        "status":"world_interface_active",
        "time":str(datetime.now())
    }
)

