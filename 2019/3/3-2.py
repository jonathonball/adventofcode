#!/usr/bin/env python3

import sys
import math
import json

class Point:

    def __init__(self, location, wire, x, y):
        self.location = location
        self.wire = wire
        self.x = x
        self.y = y
        self.length = {}

    def distance_from_center(self):
        self.distance_from_center = math.fabs(self.x) + math.fabs(self.y)

    def set_length(self, wire, length):
        self.length[wire] = length

    def __str__(self):
        return json.dumps({
            "location": self.location,
            "x": self.x,
            "y": self.y,
            "wire": self.wire,
            "length": self.length
        })

class Panel:

    def __init__(self):
        self.data = {}
        self.intersections = []

    def location(self, x, y):
        """Return string with index for self.data"""
        return str(x) + ":" + str(y)

    def get(self, x, y):
        """Return a Point object or None"""
        location = self.location(x, y)
        try:
            return self.data[location]
        except KeyError:
            return None

    def set(self, x, y, wire, length):
        """Create a new wire segment or update an existing one"""
        existing = self.get(x, y)
        if not existing:
            location = self.location(x, y) 
            point = Point(location, wire, x, y)
            point.set_length(wire, length)
            self.data[location] = point
        elif existing.wire != wire:
            existing.wire = "Intersection"
            existing.distance_from_center()
            existing.set_length(wire, length)
            existing.combo = existing.length[0] + existing.length[1]

    def reset(self):
        """Reset for new wire"""
        self.x = 0
        self.y = 0

    def add_wire(self, wire, data):
        """Parse vector data for new wire"""
        self.reset()
        length = 0
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
                length += 1
                self.set(self.x, self.y, wire, length)

    def gather_intersections(self):
        """Gather identified intersections into a list"""
        self.intersections = [
            self.data[key]
            for key in self.data.keys() if self.data[key].wire == "Intersection"
        ]

    def find_shortest_manhatten(self):
        """Find the intersection with the shortest distance from 0,0"""
        shortest = self.intersections[0].distance_from_center
        for intersection in self.intersections:
            if intersection.distance_from_center < shortest:
                shortest = intersection.distance_from_center
        return shortest

    def find_shortest_combo(self):
        """Find the intersection with the shortest length from 0,0 for both wires"""
        shortest = self.intersections[0].combo
        for intersection in self.intersections:
            if intersection.combo < shortest:
                shortest = intersection.combo
        return shortest

panel = Panel()

wires = [ line.strip().split(',') for line in sys.stdin ]
for wire, data in enumerate(wires):
    panel.add_wire(wire, data)

panel.gather_intersections()
print(panel.find_shortest_combo())

