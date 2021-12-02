#!/usr/bin/env python3

from collections import deque

file = open( './input.txt' )
lines = deque( [ int( value ) for value in file.readlines() ] )
last  = [ lines.popleft(), lines.popleft(), lines.popleft() ]
total = 0
while lines:
  current = last[1:] + [ lines.popleft() ]
  if ( sum( current ) > sum( last ) ):
    total += 1
  last = current
print (total)
