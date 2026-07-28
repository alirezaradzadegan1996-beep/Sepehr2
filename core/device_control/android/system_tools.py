import subprocess


def notify(title="Sepehr2", content="Hello"):

    subprocess.call([
        "termux-notification",
        "--title",
        title,
        "--content",
        content
    ])

    return {
        "status":"notification_sent"
    }


def clipboard_get():

    try:
        out = subprocess.check_output(
            ["termux-clipboard-get"],
            text=True
        )

        return {
            "clipboard": out
        }

    except Exception as e:
        return {
            "error": str(e)
        }


def clipboard_set(text):

    subprocess.run(
        ["termux-clipboard-set"],
        input=text,
        text=True
    )

    return {
        "status":"clipboard_updated"
    }
