from .debugable import Debugable

class RotatingNumber(Debugable):
    def __init__(self, debug=False):
        self.debug_mode = debug
        self.value = 50
        self.minimum = 0
        self.maximum = 99
        self.zero_count = 0

    def rotate(self, direction, amount):
        self.debug(f"Rotating {direction} by {amount}.")
        if direction == 'L':
            self.value = (self.value - amount) % (self.maximum + 1)
        else:
            self.value = (self.value + amount) % (self.maximum + 1)
        self.debug(f"New value: {self.value}")
        if self.value == 0:
            self.zero_count += 1
