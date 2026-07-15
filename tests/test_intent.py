from core.intent import detect_intent

print("=== Intent Test ===")

assert detect_intent("سلام") == "greeting"
assert detect_intent("سرعت نور چقدره") == "knowledge"
assert detect_intent("اسم من علیرضاست") == "memory"
assert detect_intent("من کی هستم") == "memory"

print("PASS")
