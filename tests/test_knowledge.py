from core.knowledge import search_knowledge

print("=== Knowledge Test ===")

answer = search_knowledge("دمای سطح زهره چقدر است؟")

assert answer is not None
assert "464" in answer

print("PASS")
