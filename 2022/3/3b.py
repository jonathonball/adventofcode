import math
import string

file = open('./input.txt')

def getPriority(letter):
  return string.ascii_letters.index(letter) + 1

lines = file.readlines()
total = 0
for index in range(0, len(lines), 3):
  a = set(lines[index].strip())
  b = set(lines[index + 1].strip())
  c = set(lines[index + 2].strip())
  u = a & b & c
  total += getPriority(u.pop())
print(total)
