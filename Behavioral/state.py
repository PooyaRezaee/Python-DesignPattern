"""
    State
"""

class State:
    def operate(self):
        print(f"Turning Device To {self.status}")

class TurnOff(State):
    def __init__(self,device):
        self.device = device
        self.status = 'off'

    def change_state(self):
        self.device.state = self.device.on
        self.device.is_on = False

class TurnOn(State):
    def __init__(self,device):
        self.device = device
        self.status = 'on'

    def change_state(self):
        self.device.state = self.device.off
        self.device.is_on = True

class Device:
    def __init__(self):
        self.on = TurnOn(self)
        self.off = TurnOff(self)
        self.state = self.on
        self.is_on = False

    def press(self):
        self.state.operate()
        self.state.change_state()

    def status(self):
        if self.is_on:
            print("Device Is On")
        else:
            print("Device Is Off")


device = Device()
device.status()
device.press()
device.status()
