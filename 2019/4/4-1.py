#!/usr/bin/env python3

class FuelDepotCracker:

    def __init__(self):
        self.minimum  = 271973
        self.maximum  = 785961
        self.position = self.minimum

    def is_valid(self, value):
        """Returns boolean is valid fuel depot password?"""
        has_duplicate = False
        numbers = [n for n in str(value)]
        for index in range(1, 6):
            if numbers[index - 1] == numbers[index]:
                has_duplicate = True
            if numbers[index - 1] > numbers[index]:
                return False
        return has_duplicate

    def check_values(self):
        """Iterates through all potential values to determine valid passwords"""
        self.winners = []
        for candidate in range(self.minimum, self.maximum + 1):
            if self.is_valid(candidate):
                self.winners.append(candidate)

    def number_of_winners(self):
        return len(self.winners)

cracker = FuelDepotCracker()
cracker.check_values()
print(cracker.number_of_winners())
