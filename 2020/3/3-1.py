#!/usr/bin/python3

import sys

class Matrix:

    def __init__(self, rise, run):
        self.data  = []
        self.rise  = rise
        self.run   = run
        self.x     = 0
        self.y     = 0
        self.trees = 0

    def import_data(self, stream):
        for string in stream:
            characters = string.strip()
            row = self.create_row(characters)
            self.data.append(row)

    def create_row(self, data):
        return [ character for character in data ]

    def count_trees(self):
        number_of_trees = 0
        if self.is_tree():
            number_of_trees += 1
        while(self.move_down_slope()):
            if self.is_tree():
                number_of_trees += 1
        self.trees = number_of_trees

    def is_tree(self):
        if self.data[self.y][self.x] == "#":
            return True
        return False

    def column_width(self, index):
        return len(self.data[index])

    def move_down_slope(self):
        number_of_rows = len(self.data)
        self.y += self.rise
        if self.y >= number_of_rows:
            return False
        number_of_columns = self.column_width(self.y)
        self.x += self.run
        if self.x >= number_of_columns:
            self.x -= number_of_columns
        return True
    
m = Matrix(1, 3)
m.import_data(sys.stdin)
m.count_trees()
print(m.trees)