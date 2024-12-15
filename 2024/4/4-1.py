import sys
import argparse

class Node:

    rank_list = [ 'X', 'M', 'A', 'S' ]

    def __init__(self, x, y, value, debug):
        self.key = "%d,%d" %  (int(x), int(y))
        self.x = int(x)
        self.y = int(y)
        self.index = [y, x]
        self.value = value
        self.rank_index = self.getRankIndex()
        self.debug = debug
        self.neighbors = {}
        self.needsNeighbors = False
        if self.debug:
            print("Creating node: %s" % self)

    def addNeighbor(self, neighbor):
        if self.debug:
            print("Add " + neighbor.key + " to " + self.key)
        self.neighbors[neighbor.key] = neighbor

    def getLastRankIndex(self):
        return len(self.rank_list - 1)

    def getRankIndex(self):
        for i, rank in enumerate(self.rank_list):
            if self.value == rank:
                return i

    def getNextRankIndex(self):
        pass

    def nextRank(self):
        if self.value == self.getLastRankIndex():
            return True
        for key, value in self.neighbors:


    def __str__(self):
        return "(%s) %s [%d] x %d" % (self.key, self.value, self.needsNeighbors, len(self.neighbors))

def four(args, data):
    y_length = len(data)
    for y, line in enumerate(data):
        x_length = len(line)
        for x, char in enumerate(line):
            data[y][x] = node = Node(x,y,char,args.debug)
            if (x > 0 and x < x_length - 1) and (y > 0 and y < y_length - 1 ):
                node.needsNeighbors = True

    for y, line in enumerate(data):
        for x, node in enumerate(line):
            if node.needsNeighbors:
                if args.debug:
                    print("start " + node.key + ": ")
                for i in range(x - 1, x + 2):
                    for j in range(y - 1, y + 2):
                        if (i == x and j == y):
                            pass
                        else:
                            node.addNeighbor(data[j][i])

    for line in data:
        for node in line:
            print(node)

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
    return [ list(line) for line in rawdata.split() ]

def main():
    args = get_args()
    rawdata = get_raw_data(args)
    data = parse_input(args, rawdata)
    return four(args, data)

if __name__ == "__main__":
    sys.exit(main())
