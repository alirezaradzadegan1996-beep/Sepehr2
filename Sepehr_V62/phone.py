import os

def execute(cmd):

    if cmd == "wifi":
        os.system("termux-wifi-enable true")
        return "وای فای روشن شد 📡"

    if cmd == "bluetooth":
        os.system("termux-bluetooth-scaninfo")
        return "بلوتوث بررسی شد 📶"

    if cmd == "camera":
        os.system("termux-camera-photo pic.jpg")
        return "عکس گرفته شد 📷"

    if cmd == "sms":
        os.system("termux-sms-send -n 123456 سلام از سپهر")
        return "پیام ارسال شد 📩"

    if cmd == "call":
        os.system("termux-telephony-call 123456")
        return "در حال تماس 📞"

    return "دستور نامشخص"
