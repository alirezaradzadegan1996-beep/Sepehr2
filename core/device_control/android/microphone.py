import subprocess
import os

def record(seconds=5, name="record.wav"):

    os.makedirs(
        "storage/audio",
        exist_ok=True
    )

    path = f"storage/audio/{name}"

    subprocess.call([
        "termux-microphone-record",
        "-l",
        str(seconds),
        "-f",
        path
    ])

    return {
        "status":"recorded",
        "file":path
    }
