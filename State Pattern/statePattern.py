#State Inteface
class TrafficLightState:
    def handle(self, context):
        raise NotImplementedError

#Concrete State Class
class GreenLightState(TrafficLightState):
    def handle(self, context):
        print("Green light! Go!")
        context.set_state(YellowLightState())

class YellowLightState(TrafficLightState):
    def handle(self, context):
        print("Yellow light! Slow down!")
        context.set_state(RedLightState())

class RedLightState(TrafficLightState):
    def handle(self, context):
        print("Red light! Stop!")
        context.set_state(GreenLightState())

#Context Class
class TrafficLight:
    def __init__(self):
        self._state = GreenLightState()

    def set_state(self, state):
        self._state = state

    def change(self):
        self._state.handle(self)

traffic_light = TrafficLight()
for _ in range(6):
    traffic_light.change()
