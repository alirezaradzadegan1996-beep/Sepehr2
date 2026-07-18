from core.cortex.bootstrap import boot
from core.cortex.cortex import cortex


print("=== Cortex Test ===")

boot()

services = cortex.services()

assert "memory" in services
assert "knowledge" in services
assert "reasoning" in services
assert "router" in services
assert "planner" in services
assert "health" in services


health = cortex.get("health")

status = health.check()

print(status)

assert "memory" in status
assert "router" in status


print("PASS")
