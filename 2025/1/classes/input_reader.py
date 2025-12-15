import sys

class InputReader:
    def __init__(self, source=None):
        if not source:
            self.source = sys.stdin

    def __iter__(self):
        return self

    def __next__(self):
        raw = self.source.readline()
        if not raw:
            raise StopIteration
        line = raw.strip()
        return line[0], int(line[1:])
