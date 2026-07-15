"""
Sepehr2 System Bus
Shared data + Event Bus
"""


class SystemBus:

    def __init__(self):
        self.data = {}
        self.events = {}
        self.history = []

    # -------------------------
    # Shared Data
    # -------------------------

    def set(self, key, value):
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def remove(self, key):
        if key in self.data:
            del self.data[key]

    def clear(self):
        self.data.clear()

    # -------------------------
    # Events
    # -------------------------

    def subscribe(self, event, callback):
        self.events.setdefault(event, []).append(callback)

    def unsubscribe(self, event, callback):
        if event not in self.events:
            return

        if callback in self.events[event]:
            self.events[event].remove(callback)

    def publish(self, event, *args, **kwargs):
        self.history.append(event)

        for callback in self.events.get(event, []):
            try:
                callback(*args, **kwargs)
            except Exception as e:
                print(f"[SystemBus] {event} -> {e}")

    # -------------------------
    # Status
    # -------------------------

    def status(self):
        return {
            "data": list(self.data.keys()),
            "events": list(self.events.keys()),
            "history": len(self.history),
        }


bus = SystemBus()
