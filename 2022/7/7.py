#!/usr/bin/env python3

import argparse
import pathlib
import sys

# parser = argparse.ArgumentParser()
# parser.add_argument("file", type=pathlib.Path, help="Input file")
# args = parser.parse_args()

# if not args.file.is_file():
#   print(args.file, end='')
#   print(" is not a file.")
#   sys.exit(255)

# try:
#   file = open(args.file)
# except Exception as err:
#   print(str(err))
#   print("Could not open that file. :(")
#   sys.exit(255)

data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""

class File:
  def __init__(self, name, size, parent):
    self.name = name
    self.size = int(size)
    self.isFlle = True
    self.parent = parent
  def getSize(self) -> int:
    return self.size

class Dir:
  def __init__(self, name, parent=None):
    self.name = name
    self.children = {}
    self.isFile = False
    self.parent = parent
  def add(self, item):
    item.parent = self
    self.children[item.name] = item
    return self.children[item.name]
  def getSize(self) -> int:
    total = 0
    for name in self.children.keys():
      total += self.children[name].getSize()
    return total

fs = None
for line in data.split("\n"):
  line = line.strip()
  print('input: ' + line)
  command = line[2:4]
  if command == 'cd' and fs == None:
    path = line[5:]
    fs = Dir(path)
  elif command == 'cd':
    path = line[5:]
    if path == '..':
      fs == fs.parent
      print("\tchange to " + fs.name)
    else:
      print("\tchange to " + path)
      fs = fs.children[path]
  elif command == 'ls':
    pass
  else:
    data, name = line.split()
    print("\tcollecting", data, name, "into", fs.name)
    if data == 'dir':
      fs.add(Dir(name))
    else:
      fs.add(File(name, data, fs))
    
