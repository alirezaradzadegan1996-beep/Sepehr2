

class EventBus:

    def emit(self,event):
        return {
            "event":event,
            "status":"UNIFIED_EVENT_BUS_ACTIVE"
        }


event_bus=EventBus()

