import subprocess
import json


def volume_info():

    try:
        out = subprocess.check_output(
            ["termux-volume"],
            text=True
        )

        return json.loads(out)

    except Exception as e:
        return {
            "error": str(e)
        }


def set_volume(stream="music", level=5):

    subprocess.call([
        "termux-volume",
        stream,
        str(level)
    ])

    return {
        "stream": stream,
        "level": level
    }


def media_key(key):

    subprocess.call([
        "termux-media-player",
        key
    ])

    return {
        "media": key
    }
