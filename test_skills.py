from core.memory import Memory
from core.skills.app_builder import AppBuilder

memory = Memory()

app_skill = AppBuilder(memory)

result = app_skill.run({"name": "calculator_app"})

print(result)
