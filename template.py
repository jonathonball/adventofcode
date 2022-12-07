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


for rawInput in file.readlines():
  pass
