#!/usr/bin/env python3

import sys
import argparse
import collections

def two(data):
    left, right = data
    right_counts = collections.defaultdict(int)
    similarity = 0
    for number in right:
        right_counts[number] += 1
        print(number, right_counts)
    for number in left:
        similarity += number * right_counts[number]
    print(similarity)
    return 0

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', default='.\\input.txt')
    parser.add_argument('-d', '--delimiter', default='\n')
    return parser.parse_args()

def get_raw_data(args):
    try:
        with open(args.filename, 'r') as file:
            rawdata = file.read()
    except FileNotFoundError:
        print("Unable to read input file")
        return 1
    return rawdata

def parse_input(args, rawdata):
    lines = rawdata.split(args.delimiter)
    left, right = [[], []]
    for line in lines:
        west, east = line.split()
        left.append(int(west))
        right.append(int(east))
    return left, right

def main():
    args = get_args()
    rawdata = get_raw_data(args)
    data = parse_input(args, rawdata)
    return two(data)

if __name__ == "__main__":
    sys.exit(main())
