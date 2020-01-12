#!/usr/bin/env python3

import sys

class IntCodePc:

    def __init__(self):
        self.read_input()
        self.instruction_pointer = 0

    def run(self):
        while self.instruction_pointer < self.size:
            self.fetch()
            if self.opcode == 99:
                print(self.read(0))
                sys.exit()
            elif self.opcode == 1:
                self.write(self.output, (self.param_a + self.param_b))
            elif self.opcode == 2:
                self.write(self.output, (self.param_a * self.param_b))
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

    def read(self, instruction_pointer):
        return int(self.mem[instruction_pointer])

    def deref(self, instruction_pointer):
        return self.mem[self.read(instruction_pointer)]

    def write(self, instruction_pointer, value):
        self.mem[instruction_pointer] = value

    def fetch(self):
        self.opcode = self.read(self.instruction_pointer)
        self.param_a = self.deref(self.instruction_pointer + 1)
        self.param_b = self.deref(self.instruction_pointer + 2)
        self.output = self.read(self.instruction_pointer + 3)
        self.instruction_pointer += 4

pc = IntCodePc()
print(pc.run())
