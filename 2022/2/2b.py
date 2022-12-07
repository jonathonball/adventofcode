#!/usr/bin/env python3

file = open('./input.txt')

# A X ROCK
# B Y PAPER
# C Z SKIZORS

solutionMap = {
  'A': {
    'name': 'rock',
    'defeats': 'C',
    'loses': 'B',
    'value': 1
  },
  'B': {
    'name': 'paper',
    'defeats': 'A',
    'loses': 'C',
    'value': 2
  },
  'C': {
    'name': 'scissors',
    'defeats': 'B',
    'loses': 'A',
    'value': 3
  }
}

score = 0
for rawInput in file.readlines():
  opponentChoice, myChoice = [ s.strip() for s in rawInput.split(' ') ]
  match myChoice:
    case 'X': # lose
      myChoice = solutionMap[opponentChoice]['defeats']
    case 'Y': # draw
      myChoice = opponentChoice
    case 'Z': # win
      myChoice = solutionMap[opponentChoice]['loses']
  score += solutionMap[myChoice]['value']
  if opponentChoice == myChoice:
    score += 3
  if solutionMap[myChoice]['defeats'] == opponentChoice:
    score += 6

print(score)
