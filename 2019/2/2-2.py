#!/usr/bin/env python3

from IntCodePc import IntCodePc

pc = IntCodePc.Pc()
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
