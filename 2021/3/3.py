#!/usr/bin/env python3
import sys

data_sample = sys.stdin.readline().strip()
sample_length = len( data_sample )
totals = [0] * sample_length
num_lines = 1
for binary in sys.stdin:
  binary = binary.strip()
  for index, value in enumerate( binary ):
    if value == "1":
      totals[index] += 1
  num_lines += 1
threshold = int( num_lines / 2 )
gamma = [''] * sample_length
epsilon = [''] * sample_length
for index, total in enumerate( totals ):
  if total > threshold:
    gamma[index] = "1"
    epsilon[index] = "0"
  else:
    gamma[index] = "0"
    epsilon[index] = "1"
gamma_int = int( ''.join( gamma ), 2 )
epsilon_int = int( ''.join( epsilon ), 2 )
print ( gamma_int * epsilon_int )
