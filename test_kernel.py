from core.kernel import Kernel


class DummyModule:
    def start(self):
        print("DummyModule started")

    def stop(self):
        print("DummyModule stopped")

    def handle_event(self, event):
        print("Event received:", event)


kernel = Kernel()

kernel.register_module("dummy", DummyModule())

kernel.start()

kernel.send_event("HELLO_SEPEHR")

kernel.stop()
