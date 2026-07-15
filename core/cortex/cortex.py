"""
Sepehr2 Cortex
مرکز مدیریت تمام سرویس‌های سیستم
"""

from .registry import registry
from .engine import CortexEngine


class Cortex:

    def __init__(self):
        self.registry = registry
        self.engine = CortexEngine(self.registry)

    def register(self, name, service):
        self.registry.register(name, service)

    def unregister(self, name):
        self.registry.unregister(name)

    def has(self, name):
        return self.registry.has(name)

    def get(self, name):
        return self.registry.get(name)

    def execute(self, name, *args, **kwargs):
        return self.engine.execute(name, *args, **kwargs)

    def services(self):
        return self.registry.list()

    def status(self):
        return {
            "services": self.registry.list(),
            "engine": self.engine.report(),
        }


cortex = Cortex()
