#!/usr/bin/env python3

class Elf:
  def __init__(self) -> None:
    self.food = 0
  def addFood(self, food: int) -> None:
    self.food += food
  def getFood(self) -> int:
    return self.food

def elfSort(elf):
  return elf.getFood()

elves = []
elf = Elf()

file = open('./input.txt')
for rawInput in file.readlines():
  if rawInput == "\n":
    elves.append(elf)
    elf = Elf()
  else:
    food = int(rawInput)
    elf.addFood(food)

elves.sort(key=elfSort)
total = 0
for elf in elves[-3:]:
  total += elf.getFood()
print(total)