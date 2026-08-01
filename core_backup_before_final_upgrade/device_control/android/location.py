import json
import subprocess

def get_location():
    try:
        out = subprocess.check_output(
            ["termux-location", "-p", "gps"],
            text=True
        )
        return json.loads(out)
    except Exception as e:
        return {"error": str(e)}
