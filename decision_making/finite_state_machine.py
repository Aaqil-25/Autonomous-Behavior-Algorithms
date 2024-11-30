class State:
    def __init__(self, name):
        self.name = name

    def on_enter(self):
        print(f"Entering {self.name} state.")

    def on_exit(self):
        print(f"Exiting {self.name} state.")

class FiniteStateMachine:
    def __init__(self):
        self.states = {}
        self.current_state = None

    def add_state(self, state):
        self.states[state.name] = state

    def set_state(self, state_name):
        if self.current_state:
            self.current_state.on_exit()
        self.current_state = self.states.get(state_name)
        if self.current_state:
            self.current_state.on_enter()

# Example usage
if __name__ == "__main__":
    idle = State("Idle")
    moving = State("Moving")

    fsm = FiniteStateMachine()
    fsm.add_state(idle)
    fsm.add_state(moving)

    fsm.set_state("Idle")
    fsm.set_state("Moving")
