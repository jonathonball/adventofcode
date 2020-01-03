import sys
import math

def calculate_fuel(mass):
    return math.floor(mass / 3) - 2

total = 0
for mass in [int(line.strip()) for line in sys.stdin]:
    total += calculate_fuel(mass)
print(total)
