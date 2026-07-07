class ContextMemory:
    def __init__(self):
        self.context = []

    # ذخیره پیام‌ها
    def add(self, text):
        self.context.append(text)

        # محدود نگه داشتن حافظه (جلوگیری از قاطی شدن)
        if len(self.context) > 20:
            self.context = self.context[-20:]

    # تشخیص اینکه آیا باید context استفاده شود یا نه
    def detect_context(self, text):
        return len(self.context) > 0

    # گرفتن context به صورت رشته
    def get_context(self):
        if not self.context:
            return ""
        return self.context[-1]

    # 🧠 پاک کردن کامل context (خیلی مهم برای پروژه جدید)
    def clear(self):
        self.context = []
