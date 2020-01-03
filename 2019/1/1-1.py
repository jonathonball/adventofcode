#!/usr/bin/env python3

import sys
import math


def read_mass_file():
    return [int(line.strip()) for line in sys.stdin]


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2

total = 0
for mass in read_mass_file():
    total += calculate_fuel(mass)
print(total)
