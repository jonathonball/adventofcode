#!/usr/bin/python3

import sys

numbers = []
target = 2020

# Read integers into a list
for line in sys.stdin:
    number = int(line.strip())
    numbers.append(number)

for a in numbers:
    for b in numbers:
        for c in numbers:
            if a + b + c == target:
                result = a * b * c
                print(f"{a} * {b} * {b} = {result}")
                sys.exit()

