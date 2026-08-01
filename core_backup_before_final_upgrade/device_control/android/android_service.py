from .battery import get_battery
from .toast import show
from .camera import capture
from .apps import open_app
from .files import ls,mkdir,rm,info
from .location import get_location
from .network import wifi_info,wifi_scan
from .microphone import record
from .hardware import torch,vibrate
from .media import volume_info,set_volume,media_key
from .system_tools import notify,clipboard_get,clipboard_set
from .communication import call,send_sms,sms_list
from .sensors import get_sensors,read_sensor

class AndroidService:

    name = "android"

    def boot(self):
        print("[Android] Ready")

    def info(self):
        return {
            "name": "android",
            "features": [
                "battery",
                "toast",
                "camera",
                "apps"
            ]
        }

    def execute(self, text):

        t = text.lower()

        if "باتری" in t:
            return get_battery()

        if "toast" in t:
            show("Sepehr2")
            return "Toast Sent"

        if "عکس" in t or "دوربین" in t:
            return capture()

        if "تنظیمات" in t:
            open_app("تنظیمات")
            return "Settings Opened"

        if "کروم" in t:
            open_app("کروم")
            return "Chrome Opened"

        
        if "لیست فایل" in t:
            return ls("~/")

        if "ساخت پوشه" in t:
            return mkdir("~/SepehrFolder")

        if "اطلاعات فایل" in t:
            return info("~/")


        
        if "موقعیت" in t or "gps" in t:
            return get_location()


        
        if "وای فای" in t or "wifi" in t:
            return wifi_info()

        if "اسکن وای فای" in t:
            return wifi_scan()


        
        if "ضبط صدا" in t or "میکروفون" in t:
            return record()


        
        if "چراغ" in t or "فلش" in t:
            return torch(True)

        if "خاموش کردن چراغ" in t:
            return torch(False)

        if "ویبره" in t:
            return vibrate()


        
        if "صدا" in t or "ولوم" in t:
            return volume_info()

        if "زیاد کن" in t:
            return set_volume(level=10)

        if "کم کن" in t:
            return set_volume(level=2)

        if "موزیک" in t:
            return media_key("play")


        
        if "اعلان" in t:
            return notify(
                "Sepehr2",
                "Android Control Active"
            )

        if "کلیپ" in t:
            return clipboard_get()


        
        if "تماس" in t:
            return {
                "hint":"use call(number)"
            }

        if "پیامک" in t:
            return {
                "hint":"use send_sms(number,message)"
            }


        
        if "سنسور" in t:
            return get_sensors()

        if "شتاب" in t:
            return read_sensor("accelerometer")


        return None
