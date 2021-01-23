#!/usr/bin/python3

# Validate Passport
# Valid passports have all fields except "cid"
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

import sys
import re

regexes = {
    "valid_color": re.compile("^#[a-f\d]{6}"),
    "valid_height": re.compile("\d+(cm|in)"),
    "find_numbers": re.compile("\d+"),
    "find_unit": re.compile("cm|in")
}

a = "100cm"
value = re.findall(regexes["find_numbers"], a)
print(value)
unit = re.findall(regexes["find_unit"], a)
print(unit)

class Validator:

    def __init__(self, subject):
        self.rules = []
        self.subject = subject

    def add_regex_rule(self, regex):
        self.rules.append({
            "method": "regex",
            "regex":   regex
        })

    def add_range_rule(self, min, max, inclusive = False):
        self.rules.append({
            "method":    "range",
            "min":       min,
            "max":       max,
            "inclusive": inclusive
        })

    def check_range(self, rule):
        if rule["inclusive"]:
            return self.check_inclusive_range(rule)
        else:
            return self.check_exclusive_range(rule)

    def check_inclusive_range(self, rule):
        return self.subject >= rule["min"] and self.subject <= rule["max"]

    def check_exclusive_range(self, rule):
        return self.subject > rule["min"] and self.subject < rule["max"]

    def delimit_unit(self, rule, unit):
        pass

    def is_valid(self):
        for rule in self.rules:
            if rule["method"] == "regex":
                return rule["regex"].match(self.subject)
            elif rule["method"] == "range":
                return self.check_range(rule)

class Field:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def is_valid(self):
        pass

    def __str__(self):
        return self.value

class Passport:

    def __init__(self):
        self.fields = {
            "byr": None, # (Birth Year)
            "iyr": None, # (Issue Year)
            "eyr": None, # (Expiration Year)
            "hgt": None, # (Height)
            "hcl": None, # (Hair Color)
            "ecl": None, # (Eye Color)
            "pid": None, # (Passport ID)
        }
        self.required_keys = set(self.fields.keys())

    def add_field(self, key, value):
        field = Field(key, value)
        if field.is_valid():
            self.fields[key] = value

    def is_valid(self):
        for key in self.required_keys:
            if self.fields[key] == None:
                return False
        return True


# Code execution starts here
# passports = []
# passport = Passport()
# for line in sys.stdin:
#     if line == "\n":
#         if passport.is_valid():
#             passports.append(passport)
#         passport = Passport()
#     else:
#         new_fields = line.strip().split(" ")
#         for new_field in new_fields:
#             key, value = new_field.split(":")
#             passport.add_field(key, value)
 
# print(len(passports))