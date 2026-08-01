import subprocess
import json

def get_battery():

    out = subprocess.check_output(
        ["termux-battery-status"]
    ).decode()

    return json.loads(out)
