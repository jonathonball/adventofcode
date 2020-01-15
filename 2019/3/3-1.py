#!/usr/bin/env python3

import sys
import math


class Point:

    def __init__(self, panel, location, wire, x, y):
        self.panel = panel
        self.location = location
        self.wire = wire
        self.x = x
        self.y = y

    def distance(self):
        self.distance = math.fabs(self.x) + math.fabs(self.y)


class Panel:

    def __init__(self):
        self.data = {}
        self.intersections = {}
        self.total = 0

    def location(self, x, y):
        return str(x) + ":" + str(y)

    def get(self, x, y):
        location = self.location(x, y)
        try:
            return self.data[location]
        except KeyError:
            return None

    def set(self, x, y, wire):
        location = self.location(x, y) 
        existing = self.get(x, y)
        if not existing:
            point = Point(self, location, wire, x, y)
            self.data[location] = point
            return point
        if existing.wire != wire:
            existing.wire = "Intersection"
            existing.distance()
        return existing

    def reset(self):
        self.x = 0
        self.y = 0

    def add_wire(self, wire, data):
        self.reset()
        
        for vector in data:
            direction = vector[0]
            magnitude = int(vector[1:])
            for _ in range(magnitude):
                if direction == "U":
                    self.y += 1
                elif direction == "D":
                    self.y -= 1
                elif direction == "L":
                    self.x -= 1
                else:
                    self.x += 1
                self.set(self.x, self.y, wire)

panel = Panel()
wires = [ line.strip().split(',') for line in sys.stdin ]
for wire, data in enumerate(wires):
    panel.add_wire(wire, data)

intersections = [
    panel.data[key]
    for key in panel.data.keys() if panel.data[key].wire == "Intersection"
]

shortest = intersections[0].distance
for intersection in intersections:
    if intersection.distance < shortest:
        shortest = intersection.distance
print(shortest)
