#!/usr/bin/env python3

file = open( './input.txt' )
lines = [ int( value ) for value in file.readlines() ]
last = lines[0]
total = 0
for line in lines[1:]:
    if line > last:
        total += 1
    last = line
print( total )


