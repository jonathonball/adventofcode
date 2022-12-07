#!/usr/bin/env python3

import argparse
import pathlib
import sys

parser = argparse.ArgumentParser()
parser.add_argument("file", type=pathlib.Path, help="Input file")
args = parser.parse_args()

if not args.file.is_file():
  print(args.file, end='')
  print(" is not a file.")
  sys.exit(255)

try:
  file = open(args.file)
except Exception as err:
  print(str(err))
  print("Could not open that file. :(")
  sys.exit(255)

positions = ['start', 'stop']

def createStartStopDict(input: str) -> dict:
  return { position: int(value) for position, value in zip(positions, input.split('-')) }

total = 0
for rawInput in file.readlines():
  left, right = [ string.strip() for string in rawInput.split(',') ]
  left = createStartStopDict(left)
  right = createStartStopDict(right)
  if left['start'] <= right['start'] and left['stop'] >= right['stop']:
    total += 1
  elif right['start'] <= left['start'] and right['stop'] >= left['stop']:
    total += 1
print(total)
