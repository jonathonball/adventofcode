import math
import string

file = open('./input.txt')

def getPriority(letter):
  return string.ascii_letters.index(letter) + 1

total = 0
for rawInput in file.readlines():
  input = rawInput.strip()
  mid = math.floor(len(input) / 2)
  left = set(input[:mid])
  right = set(input[mid:])
  u = left & right
  total += getPriority(u.pop())
print(total)
