import subprocess


def call(number):

    subprocess.call([
        "termux-telephony-call",
        number
    ])

    return {
        "status":"calling",
        "number":number
    }


def send_sms(number, message):

    subprocess.call([
        "termux-sms-send",
        "-n",
        number,
        message
    ])

    return {
        "status":"sms_sent",
        "number":number
    }


def sms_list():

    try:
        out = subprocess.check_output(
            ["termux-sms-list"],
            text=True
        )

        return out

    except Exception as e:
        return {
            "error":str(e)
        }
