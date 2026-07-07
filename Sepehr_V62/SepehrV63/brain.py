import random
import json

MEM_FILE = "memory.json"


def load_memory():
    try:
        return json.load(open(MEM_FILE, "r"))
    except:
        return {}


def save_memory(mem):
    json.dump(mem, open(MEM_FILE, "w"), ensure_ascii=False, indent=2)


def brain(text):

    text = text.lower().strip()
    mem = load_memory()

    # --- یاد گرفتن اسم کاربر ---
    if "اسم من" in text:
        name = text.replace("اسم من", "").strip()
        mem["user_name"] = name
        save_memory(mem)
        return f"خوشبختم {name} 😊"

    # --- استفاده از اسم ذخیره شده ---
    if "اسمت چیه" in text:
        return "من سپهر هستم 🤖"

    # --- سلام ---
    if "سلام" in text:
        if "user_name" in mem:
            return f"سلام {mem['user_name']} 👋"
        return "سلام 👋 من سپهر هستم"

    # --- خوبی ---
    if "خوبی" in text:
        return random.choice([
            "خوبم 😊 تو خوبی؟",
            "اوکی هستم 👍 تو چطوری؟",
            "حالم خوبه 🤖 تو خوبی؟"
        ])

    # --- حال کاربر ---
    if "من خوبم" in text:
        return "خوشحالم 😊"

    # --- کنترل گوشی ---
    if "وای فای" in text:
        return "wifi"

    if "دوربین" in text:
        return "camera"

    if "پیام" in text:
        return "sms"

    if "تماس" in text:
        return "call"

    # --- یادگیری ساده ---
    if text not in mem:
        mem[text] = "یاد گرفتم"
        save_memory(mem)

    return random.choice([
        "جالبه 🤔",
        "متوجه شدم 👍",
        "باشه، یاد گرفتم",
        "اوکی 👌"
    ])
