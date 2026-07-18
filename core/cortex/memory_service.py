from core.personal_memory import (
    remember,
    memory_summary,
    forget,
)

from core.cortex.service import Service


class MemoryService(Service):

    name = "memory"

    def remember(self, key, value):
        return remember(key, value)

    def summary(self):
        return memory_summary()

    def forget(self, key):
        return forget(key)

    def handle(self, text):

        text = text.strip()

        if "من کی هستم" in text:
            return self.summary()

        return None
