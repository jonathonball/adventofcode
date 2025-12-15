class RotatingNumber:
    def __init__(self):
        self.value = 50
        self.minimum = 0
        self.maximum = 99
        self.zero_count = 0
        self.zero_pass = 0

    def rotate(self, direction, amount):
        if direction == 'L':
            self.value = (self.value - amount) % (self.maximum + 1)
        else:
            self.value = (self.value + amount) % (self.maximum + 1)
        if self.value == 0:
            self.zero_count += 1
