import sys

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

class Challenge:
    def __init__(self, debug=False):
        self.debug = debug
        if self.debug:
            print("Debug mode is ON")
    
    def execute(self):
        self.safe = RotatingNumber()
        self.data = InputReader(sys.stdin)
        for direction, amount in self.data:
            print(f"Rotating {direction} by {amount}.")
            self.safe.rotate(direction, amount)
            print(f"New value: {self.safe.value}")

challenge = Challenge(debug=True)
challenge.execute()