#!/usr/bin/env python3

from IntCodePc import Pc

pc = Pc()
for noun in range(0,100):
    for verb in range(0,100):
        pc.noun = noun
        pc.verb = verb
        pc.run()
        if (pc.result == 19690720):
            print("winner! ", end='')
        print(pc)
        pc.reset()
