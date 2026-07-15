from core.feedback import update_feedback
from core.personal_memory import remember

print("=== Feedback Test ===")

# فقط برای اطمینان که کلید وجود دارد
remember("test", "ok")

result = update_feedback("دمای سطح زهره", True)

assert result is True

print("PASS")
