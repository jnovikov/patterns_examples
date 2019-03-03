class State(object):
    allowed_states = []
    state_description = None

    def change_state(self, state):
        if state.state_description in self.allowed_states:
            return True
        return False


class StateOn(State):
    allowed_states = ["sleep", "off"]
    state_description = "on"


class StateOff(State):
    allowed_states = ["on"]
    state_description = "off"


class StateSleep(State):
    allowed_states = ["off", "on"]
    state_description = "sleep"


class Computer(object):
    def __init__(self, name):
        self.name = name
        self.state = StateOff()

    def change_state(self, new_state):
        if self.state.change_state(new_state):
            self.state = new_state
        else:
            print("CANT CHANGE STATE")

    def info(self):
        print(self.state.state_description)


c = Computer("ibm")
c.info()
c.change_state(StateOff())
c.change_state(StateOn())
c.info()