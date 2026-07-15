from event_bus import EventBus

bus = EventBus()

def hello(data):
    print("سلام")
    print(data)

bus.subscribe("hello", hello)

bus.publish("hello", {
    "name": "Sepehr2"
})
