import subprocess

def show(message):

    subprocess.call(
        [
            "termux-toast",
            message
        ]
    )

    return True
