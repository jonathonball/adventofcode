import sys

class Debugable:
    def __init__(self):
        self.debug_mode = False

    def debug(self, message):
        if self.debug_mode:
            print(f"{message}")

class RotatingNumber:
    def __init__(self):
        self.value = 50
        self.minimum = 0
        self.maximum = 99
        self.zero_count = 0

    def rotate(self, direction, amount):
        if direction == 'L':
            self.value = (self.value - amount) % (self.maximum + 1)
        else:
            self.value = (self.value + amount) % (self.maximum + 1)
        if self.value == 0:
            self.zero_count += 1

class InputReader:
    def __init__(self, source):
        self.source = source

    def __iter__(self):
        return self

    def __next__(self):
        raw = self.source.readline()
        if not raw:
            raise StopIteration
        line = raw.strip()
        return line[0], int(line[1:])

class Challenge(Debugable):
    def __init__(self, debug=False):
        self.debug_mode = debug

    def execute(self):
        self.safe = RotatingNumber()
        self.data = InputReader(sys.stdin)
        for direction, amount in self.data:
            self.debug(f"Rotating {direction} by {amount}.")
            self.safe.rotate(direction, amount)
            self.debug(f"New value: {self.safe.value}")

challenge = Challenge(debug=True)
challenge.execute()
print(f"Final value: {challenge.safe.zero_count}")
