#!/usr/bin/python3

import sys

total_valid = 0

for line in sys.stdin:
    raw = line.strip()
    rules, password      = raw.split(":")
    ranges, character    = rules.split(" ")
    min_range, max_range = [ int(x) for x in ranges.split("-") ]
    count                = password.count(character)
    if count >= min_range and count <= max_range:
        total_valid += 1

print(total_valid)
