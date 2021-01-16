#!/usr/bin/python3

import sys

numbers = []
target = 2020

# Read integers into a list
for line in sys.stdin:
    number = int(line.strip())
    numbers.append(number)

for left in numbers:
    for right in numbers:
        if left + right == target:
            result = left * right
            print(f"{left} * {right} = {result}")
            sys.exit()

