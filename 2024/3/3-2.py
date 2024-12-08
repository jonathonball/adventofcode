import sys
import argparse
import re

def three(args, data):
    matches = clean_matches(re.findall(r"mul\((\d+),(\d+)\)|(don't\(\))|(do\(\))", data))
    result = 0
    enabled = True
    for match in matches:
        if len(match) == 1:
            enabled = match[0] == "do()"
        elif enabled:
            a, b = [int(n) for n in match]
            result += a * b
        if args.debug:
            print(match, enabled)
    print(result)
    return 0

def clean_matches(matches):
    """Convert tuple to list and remove empty values"""
    return [[s for s in match if s != ''] for match in matches]

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
    return three(args, data)

if __name__ == "__main__":
    sys.exit(main())
