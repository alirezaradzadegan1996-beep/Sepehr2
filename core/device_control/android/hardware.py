import subprocess


def torch(state=True):

    value = "on" if state else "off"

    subprocess.call([
        "termux-torch",
        value
    ])

    return {
        "torch": value
    }


def vibrate(duration=500):

    subprocess.call([
        "termux-vibrate",
        "-d",
        str(duration)
    ])

    return {
        "vibrate": duration
    }
