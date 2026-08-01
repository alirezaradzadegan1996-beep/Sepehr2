import subprocess
import json

def wifi_info():
    try:
        out = subprocess.check_output(
            ["termux-wifi-connectioninfo"],
            text=True
        )
        return json.loads(out)
    except Exception as e:
        return {"error": str(e)}

def wifi_scan():
    try:
        out = subprocess.check_output(
            ["termux-wifi-scaninfo"],
            text=True
        )
        return json.loads(out)
    except Exception as e:
        return {"error": str(e)}
