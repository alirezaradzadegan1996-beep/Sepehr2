import subprocess
import json
import os

class AndroidService:

    def initialize(self):
        pass

    def boot(self):
        print("[Android] Ready")

    def can_handle(self, text):
        t = text.lower()
        return any(k in t for k in [
            "باتری",
            "battery",
            "toast",
            "دوربین",
            "camera",
            "عکس"
        ])

    def handle(self, text):
        t = text.lower()

        if "باتری" in t or "battery" in t:
            out = subprocess.check_output(
                ["termux-battery-status"]
            ).decode()
            return json.loads(out)

        if "toast" in t:
            subprocess.call(
                ["termux-toast", "Hello From Sepehr2"]
            )
            return "✅ Toast ارسال شد."

        if (
            "عکس" in t
            or
            "دوربین" in t
            or
            "camera" in t
        ):

            os.makedirs(
                "storage/photos",
                exist_ok=True
            )

            path = "storage/photos/photo.jpg"

            subprocess.check_call([
                "termux-camera-photo",
                "-c",
                "0",
                path
            ])

            return {
                "status":"ok",
                "photo":path
            }

        return "Android"

android_service = AndroidService()
