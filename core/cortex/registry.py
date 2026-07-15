"""
Sepehr2 Cortex Service Registry
--------------------------------
ثبت و مدیریت تمام سرویس‌های هسته پروژه
"""


class ServiceRegistry:
    def __init__(self):
        self._services = {}

    def register(self, name, service):
        if name in self._services:
            raise ValueError(f"Service '{name}' already registered.")
        self._services[name] = service

    def register_safe(self, name, service):
        if name in self._services:
            self._services[name] = service
            return False

        self._services[name] = service
        return True

    def unregister(self, name):
        return self._services.pop(name, None)

    def get(self, name):
        if name not in self._services:
            raise KeyError(f"Service '{name}' not found.")
        return self._services[name]

    def has(self, name):
        return name in self._services

    def list(self):
        return sorted(self._services.keys())

    def clear(self):
        self._services.clear()

    def count(self):
        return len(self._services)


registry = ServiceRegistry()
