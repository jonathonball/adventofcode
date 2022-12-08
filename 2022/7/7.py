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

class Dir:

  def __init__(self, name, parent=None) -> None:
    self.name = name
    self.chidren = {}
    self.parent = parent

  def cd(self, name):
    if name == "..":
      return self.parent
    else:
      if name not in self.chidren.keys():
        self.chidren[name] = Dir(name, self)
      return self.chidren[name]

  def getRoot(self):
    if self.parent == None:
      return self
    return self.parent.getRoot()

filesystem = None
lines = [ line.strip() for line in file.readlines() ]
index = 0
while index < len(lines):
  line = lines[index]
  match line[2:4]:
    case 'cd':
      command, path = line[2:].split()
      if filesystem == None:
        filesystem = dir(path)
      else:
        
    case 'ls':
      pass
  index += 1