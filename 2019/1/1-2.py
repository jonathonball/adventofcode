#!/usr/bin/env python3

import sys
import math


def read_mass_file():
    return [int(line.strip()) for line in sys.stdin]


def calculate_base_fuel(mass):
    return math.floor(mass / 3) - 2


def calculate_total_fuel(mass, carry=0):
    fuel = calculate_base_fuel(mass)
    if (fuel > 0):
        carry += fuel
        return calculate_total_fuel(fuel, carry)
    return carry

total = 0
for mass in read_mass_file():
    total += calculate_total_fuel(mass)
print(total)
