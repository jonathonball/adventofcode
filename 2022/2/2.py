#!/usr/bin/env python3

file = open('./input.txt')

# A X ROCK
# B Y PAPER
# C Z SKIZORS

solutionMap = {
  'A': {
    'name': 'rock',
    'defeats': 'C',
    'value': 1
  },
  'B': {
    'name': 'paper',
    'defeats': 'A',
    'value': 2
  },
  'C': {
    'name': 'scissors',
    'defeats': 'B',
    'value': 3
  },
  'X': 'A',
  'Y': 'B',
  'Z': 'C'
}

score = 0
for rawInput in file.readlines():
  opponentChoice, myChoice = [ s.strip() for s in rawInput.split(' ') ]
  myChoice = solutionMap[myChoice]
  score += solutionMap[myChoice]['value']
  if opponentChoice == myChoice:
    score += 3
  if solutionMap[myChoice]['defeats'] == opponentChoice:
    score += 6

print(score)
