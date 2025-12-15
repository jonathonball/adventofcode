from .debugable import Debugable
from .rotating_number import RotatingNumber
from .input_reader import InputReader

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
