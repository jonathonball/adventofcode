#!/usr/bin/python3

import sys

total_valid = 0

for line in sys.stdin:
    raw = line.strip()
    rules, password   = raw.split(":")
    ranges, character = rules.split(" ")
    slot_a, slot_b    = [ int(x) for x in ranges.split("-") ]
    if password[slot_a] == character or password[slot_b] == character:
        if not (password[slot_a] == character and password[slot_b] == character):
            total_valid += 1

print(total_valid)
