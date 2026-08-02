from core.kernel import kernel
from core.services import registry

from core.brain.router import router

from core.services.memory_service import memory_service
from core.services.android_service import android_service
from core.services.action_service import action_service
from core.services.self_completion_service import self_completion_service


registry.register("memory", memory_service)
registry.register("android", android_service)
registry.register("action", action_service)
registry.register("self_completion", self_completion_service)


kernel.register("router", router)
kernel.register("memory", memory_service)
kernel.register("android", android_service)
kernel.register("action", action_service)
kernel.register("self_completion", self_completion_service)


for s in registry.list():

    obj = registry.get(s)

    if hasattr(obj, "boot"):

        obj.boot()
