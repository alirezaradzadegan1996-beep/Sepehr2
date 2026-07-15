from core.personal_memory import remember, recall

print("=== Memory Test ===")

remember("name", "علیرضا")

assert recall("name") == "علیرضا"

print("PASS")
