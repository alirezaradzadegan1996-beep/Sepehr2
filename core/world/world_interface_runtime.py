
from core.world.world_sensor_bridge import world_sensor_bridge
from core.world.world_perception import world_perception
from core.world.world_understanding import world_understanding


class WorldInterfaceRuntime:

    def process(self, source):

        sensor = world_sensor_bridge.receive(
            source
        )

        perception = world_perception.analyze(
            sensor
        )

        situation = world_understanding.understand(
            perception
        )

        return {
            "sensor": sensor,
            "perception": perception,
            "understanding": situation,
            "status": "pass"
        }


world_interface_runtime = WorldInterfaceRuntime()
