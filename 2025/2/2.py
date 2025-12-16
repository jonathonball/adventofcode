import sys
import re

raw = sys.stdin.read().strip().split(',')
groupings = [ [int(x) for x in group.split('-')] for group in raw ]

answer = 0
for grouping in groupings:
    for number in range(grouping[0], grouping[1]+1):
        match = re.match(r"^(\d+)\1{1,}$", str(number))
        print(number, match)
        if match:
            answer += number
        
print(answer)
