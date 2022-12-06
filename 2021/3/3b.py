#!/usr/bin/env python3
import sys

data_sample = sys.stdin.readline().strip()
sample_length = len( data_sample )
totals = [0] * sample_length
data = []
for binary in sys.stdin:
  binary = binary.strip()
  for index, value in enumerate( binary ):
    if value == "1":
      totals[index] += 1

print(totals)
#for index, total in enumerate( totals ):
#gamma_int = int( ''.join( gamma ), 2 )
#epsilon_int = int( ''.join( epsilon ), 2 )
#print ( gamma_int * epsilon_int )
