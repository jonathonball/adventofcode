#!/usr/bin/env python3

import sys
import argparse

def one(input):
    left, right = input
    left.sort()
    right.sort()
    distance = 0
    for index in range(len(left)):
        distance += abs(left[index] - right[index])
    print(distance)
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
    return one(data)

if __name__ == "__main__":
    sys.exit(main())
