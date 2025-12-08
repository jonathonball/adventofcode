import sys

class RotatingNumber:
    def __init__(self):
        self.value = 50
        self.minimum = 0
        self.maximum = 99
        self.range_length = self.maximum - self.minimum

    def rotate(self, direction, amount):
        if direction == 'L':
            self.value = (self.value - amount) % (self.maximum + 1)
        else:
            self.value = (self.value + amount) % (self.maximum + 1)

    def get_value(self):
        return self.value

safe = RotatingNumber()
zero_count = 0
for line in sys.stdin:
    raw = line.strip()
    direction = raw[0]
    amount = int(raw[1:])
    safe.rotate(direction, amount)
    print(safe.get_value())
    if safe.get_value() == 0:
        zero_count += 1
print(zero_count)
