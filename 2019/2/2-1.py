#!/usr/bin/env python3

import sys

class IntCodePc:

    def __init__(self):
        self.index = 0
        self.opcode = 0
        self.input_a = 0
        self.input_b = 0
        self.output = 0
        self.read_input()

    def run(self):
        while self.index < self.size:
            self.fetch()
            if self.opcode == 99:
                print(self.read(0))
                sys.exit()
            elif self.opcode == 1:
                self.write(self.output, (self.input_a + self.input_b))
            elif self.opcode == 2:
                self.write(self.output, (self.input_a * self.input_b))
            else:
                print("bad :(")
                sys.exit(255)

    def read_input(self):
        self.mem = [
            int(num)
            for line in sys.stdin
                for num in line.strip().split(',')
        ]
        self.size = len(self.mem)

    def read(self, index):
        return int(self.mem[index])

    def deref(self, index):
        return self.mem[self.read(index)]

    def write(self, index, value):
        self.mem[index] = value

    def fetch(self):
        self.opcode = self.read(self.index)
        self.input_a = self.deref(self.index + 1)
        self.input_b = self.deref(self.index + 2)
        self.output = self.read(self.index + 3)
        self.index += 4

pc = IntCodePc()
print(pc.run())
