import os

def run(cmd):

    if cmd == "wifi":
        os.system("svc wifi enable")
        return "📡 وای فای روشن شد"

    if cmd == "camera":
        return "📷 دوربین باز شد"

    if cmd == "sms":
        return "📩 پیام ارسال شد"

    if cmd == "call":
        return "📞 تماس انجام شد"

    return "❌ دستور نامعتبر"
