from core.memory import Memory
from core.kernel import Kernel


class DummyModule:
    def start(self):
        print("DummyModule started")

    def handle_event(self, event):
        print("Module received:", event)


# ساخت حافظه
memory = Memory()

# ساخت کرنل با اتصال حافظه
kernel = Kernel(memory)

# ثبت ماژول
kernel.register_module("dummy", DummyModule())

# شروع سیستم
kernel.start()

# ذخیره مستقیم در حافظه
kernel.remember("user", "علیرضا")

# تست بازیابی
print(kernel.recall("user"))

# ارسال event
kernel.send_event("HELLO_SEPEHR")

kernel.stop()
