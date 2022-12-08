#!/usr/bin/env python3

import argparse
import pathlib
import sys
from collections import deque

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

rawInput = deque(file.readline().strip())
buffer = deque()
for i in range(4):
  buffer.append(rawInput.popleft())
index = 4
for char in rawInput:
  if len(set(buffer)) == 4:
    print(index)
    sys.exit()
  else:
    buffer.popleft()
    buffer.append(char)
    index += 1
print(index)
