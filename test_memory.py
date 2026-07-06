from core.memory import Memory

mem = Memory()

mem.save("user", "علیرضا")
mem.save("project", "Sepehr OS")

print(mem.get("user"))
print(mem.get("project"))

print(mem.show_all())
