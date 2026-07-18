from core.cortex.service import Service
from core.cortex.system_bus import bus


class EventService(Service):

    name = "events"


    def publish(self, event, *args, **kwargs):

        bus.publish(
            event,
            *args,
            **kwargs
        )


    def history(self):

        return bus.history
