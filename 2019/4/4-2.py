#!/usr/bin/env python3
import sys
class FuelDepotCracker:

    def __init__(self):
        self.minimum  = 271973
        self.maximum  = 785961
        self.position = self.minimum

    def is_valid(self, value):
        """Returns boolean is valid fuel depot password?"""
        has_duplicate = False
        numbers = [n for n in str(value)]
        repeats = self.repeated_counts(numbers)        
        if not len(repeats.keys()):
            return False
        if not self.is_sequential(numbers):
            return False
        return True

    def repeated_counts(self, numbers):
        """Return dictionary with tallies of each number repeated in the string"""
        repeated = {}
        for index, number in enumerate(numbers):
            if index != 0:
                if numbers[index - 1] == number:
                    try:
                        repeated[number] += 1
                    except KeyError:
                        repeated[number] = 2
        return self.filter_counts(repeated)

    def filter_counts(self, counts):
        """Return dictionary with only valid repeat entries"""
        results = {}
        for key in counts.keys():
            if counts[key] <= 2:
                results[key] = counts[key]
        return results

    def is_sequential(self, numbers):
        """Return boolean if thing contains sequential values"""
        for index in range(1, 6):
            if numbers[index - 1] > numbers[index]:
                return False
        return True

    def check_values(self):
        """Iterates through all potential values to determine valid passwords"""
        self.winners = []
        for candidate in range(self.minimum, self.maximum + 1):
            if self.is_valid(candidate):
                self.winners.append(candidate)

    def number_of_winners(self):
        """Return the numbe of valid passwords"""
        return len(self.winners)

cracker = FuelDepotCracker()
cracker.check_values()
print(cracker.number_of_winners())

