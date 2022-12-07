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

rawDrawings = []
doReadDrawing = True
while doReadDrawing:
  rawInput = file.readline()
  if rawInput == "\n":
    doReadDrawing = False
  else:
    rawDrawings.append(rawInput)


#numColumns = len(columns.split())
#numRows = len(rawDrawings)
columns = []
columnMap = rawDrawings.pop()

for index, value in enumerate(columnMap):
  if value.isnumeric():
    column = deque()
    for row in rawDrawings:
      if row[index].isalpha():
        column.appendleft(row[index])
    columns.append(list(column))

print(columns)

instructions = []
for rawInput in file.readlines():
  pass
