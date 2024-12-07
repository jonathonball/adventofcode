import sys
import argparse

def get_direction(x, y):
    check = y - x
    if check > 0:
        return "increasing"
    if check < 0:
        return "decreasing"
    return "level"

def get_level_direction(level):
    return get_direction(level[0], level[1])

def is_level_safe(level):
    level_direction = get_level_direction(level)
    if level_direction == "level":
        return "unsafe - no direction"
    for n in range(1, len(level)):
        direction = get_direction(level[n-1], level[n])
        if direction != level_direction:
            return "unsafe - cannot change direction"
        difference = level[n-1] - level[n]
        if abs(difference) > 3:
            return "unsafe - too large delta"
    return "safe"

def one(args, data):
    safe_reports = 0
    for level in data:
        safety_status = is_level_safe(level)
        if args.debug:
            print(safety_status)
        if safety_status == "safe":
            safe_reports += 1
    print(safe_reports)
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
        sys.exit(1)
    return rawdata

def parse_input(args, rawdata):
    lines = []
    for line in rawdata.split(args.delimiter):
        lines.append([int(n) for n in line.split(" ")])
    return lines

def main():
    args = get_args()
    rawdata = get_raw_data(args)
    data = parse_input(args, rawdata)
    return one(args, data)

if __name__ == "__main__":
    sys.exit(main())
