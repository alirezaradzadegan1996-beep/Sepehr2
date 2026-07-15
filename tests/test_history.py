from core.conversation_memory import add_message, show_history

print("=== History Test ===")

add_message(
    "سلام",
    "سلام، چطور می‌توانم کمک کنم؟"
)

history = show_history()

assert "سلام" in history

print("PASS")
