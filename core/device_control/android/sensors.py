import subprocess
import json


def get_sensors():

    try:
        out = subprocess.check_output(
            [
                "termux-sensor",
                "-l"
            ],
            text=True
        )

        return json.loads(out)

    except Exception as e:
        return {
            "error": str(e)
        }


def read_sensor(sensor, delay=1000):

    try:
        out = subprocess.check_output(
            [
                "termux-sensor",
                "-s",
                sensor,
                "-n",
                "1",
                "-d",
                str(delay)
            ],
            text=True
        )

        return json.loads(out)

    except Exception as e:
        return {
            "error": str(e)
        }
