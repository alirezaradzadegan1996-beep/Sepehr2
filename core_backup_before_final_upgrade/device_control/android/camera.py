import subprocess
import os

PHOTO_DIR="storage/photos"

def capture(name="photo.jpg",camera="0"):

    os.makedirs(PHOTO_DIR,exist_ok=True)

    path=f"{PHOTO_DIR}/{name}"

    subprocess.check_call([
        "termux-camera-photo",
        "-c",
        camera,
        path
    ])

    return path
