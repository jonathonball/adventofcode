#!/usr/bin/env python3

fp = open('./input.txt', 'r')
lines = [ line.strip().split() for line in fp.readlines() ]

distance = 0
depth = 0
for [command, value] in lines:
  value = int(value)
  if command == 'forward':
    distance += value
  elif command == 'down':
    depth += value
  else:
    depth -= value
print(distance * depth)
