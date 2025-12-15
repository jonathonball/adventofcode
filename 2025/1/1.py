from classes import Debugable
from classes import RotatingNumber
from classes import InputReader

class Challenge(Debugable):
    def __init__(self, debug=False):
        self.debug_mode = debug

    def execute(self):
        self.safe = RotatingNumber()
        self.data = InputReader()
        for direction, amount in self.data:
            self.debug(f"Rotating {direction} by {amount}.")
            self.safe.rotate(direction, amount)
            self.debug(f"New value: {self.safe.value}")

if __name__ == "__main__":
    challenge = Challenge(debug=True)
    challenge.execute()
    print(f"Final value: {challenge.safe.zero_count}")
