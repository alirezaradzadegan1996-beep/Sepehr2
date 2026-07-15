from core.chat import chat_response

print("=== Brain Test ===")

# حافظه
chat_response("اسم من علیرضاست")

answer = chat_response("من کی هستم")

assert "علیرضا" in answer

# دانش
answer = chat_response("دمای سطح زهره چقدر است?")

assert "464" in answer

print("PASS")
