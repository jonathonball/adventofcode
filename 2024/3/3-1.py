import sys
import argparse
import re

def three(data):
    muls = re.findall(r'mul\((\d+),(\d+)\)', data)
    result = 0
    for mul in muls:
        a, b = [int(n) for n in mul]
        result += a * b
    print(result)
    return 0

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', default='.\\input.txt')
    parser.add_argument('-d', '--delimiter', default='\n')
    parser.add_argument('--debug', action='store_true')
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
    return rawdata

def main():
    args = get_args()
    rawdata = get_raw_data(args)
    data = parse_input(args, rawdata)
    return three(data)

if __name__ == "__main__":
    sys.exit(main())
