#!/usr/bin/env python3

class Elf:
  def __init__(self) -> None:
    self.food = 0
  def addFood(self, food: int) -> None:
    self.food += food
  def getFood(self) -> int:
    return self.food

elves = []
elf = Elf()
max = 0
file = open('./input.txt')
for rawInput in file.readlines():
  if rawInput == "\n":
    elves.append(elf)
    if max < elf.getFood():
      max = elf.getFood()
    elf = Elf()
  else:
    food = int(rawInput)
    elf.addFood(food)

print(max)