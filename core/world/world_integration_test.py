
from core.world.sensor_core import sensor_core
from core.world.environment_model import environment_model
from core.world.situation_understanding import situation_understanding
from core.world.perception_memory import perception_memory


def run():

    sensor=sensor_core.read("camera")

    env=environment_model.update(sensor)

    situation=situation_understanding.analyze(env)

    perception_memory.save(situation)

    return {
        "sensor":sensor,
        "environment":env,
        "situation":situation,
        "status":"pass"
    }
