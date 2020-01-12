#!/usr/bin/env python3

import sys

class IntCodePc:

    def __init__(self):
        self.read_input()
        self.instruction_pointer = 0

    def run(self):
        self.write(1, self.noun)
        self.write(2, self.verb)
        while self.instruction_pointer < self.size:
            self.fetch()
            if self.opcode == 99:
                return self.read(0)
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
        self.state = [address for address in self.mem]

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

    def reset(self):
        self.instruction_pointer = 0
        self.mem = [address for address in self.state]

pc = IntCodePc()

for noun in range(0,100):
    for verb in range(0,100):
        pc.noun = noun
        pc.verb = verb
        result = pc.run()
        if (result == 19690720):
            print("winner!")
            print(result)
            print(pc.noun)
            print(pc.verb)
        pc.reset()
