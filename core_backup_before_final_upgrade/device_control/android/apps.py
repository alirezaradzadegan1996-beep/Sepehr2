import subprocess

APPS = {
    "تنظیمات": ["am", "start", "-a", "android.settings.SETTINGS"],
    "کروم": ["am", "start", "-n", "com.android.chrome/com.google.android.apps.chrome.Main"],
    "دوربین": ["am", "start", "-a", "android.media.action.IMAGE_CAPTURE"],
}

def open_app(name):
    cmd = APPS.get(name)
    if not cmd:
        return False

    subprocess.call(cmd)
    return True
