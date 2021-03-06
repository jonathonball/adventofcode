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

    def distance_from_center(self):
        self.distance_from_center = math.fabs(self.x) + math.fabs(self.y)


class Panel:

    def __init__(self):
        self.data = {}
        self.intersections = {}
        self.total = 0

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

    def set(self, x, y, wire):
        """Create a new wire segment or update an existing one"""
        location = self.location(x, y) 
        existing = self.get(x, y)
        if not existing:
            point = Point(self, location, wire, x, y)
            self.data[location] = point
            return point
        if existing.wire != wire:
            existing.wire = "Intersection"
            existing.distance_from_center()
        return existing

    def reset(self):
        """Reset for new wire"""
        self.x = 0
        self.y = 0

    def add_wire(self, wire, data):
        """Parse vector data for new wire"""
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


panel = Panel()

wires = [ line.strip().split(',') for line in sys.stdin ]
for wire, data in enumerate(wires):
    panel.add_wire(wire, data)

panel.gather_intersections()
print(panel.find_shortest_manhatten())

