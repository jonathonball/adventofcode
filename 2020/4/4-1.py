#!/usr/bin/python3

# Validate Passport
# Valid passports have all fields except "cid"

import sys

class Field:

    valid_fields = {
        "byr", # (Birth Year)
        "iyr", # (Issue Year)
        "eyr", # (Expiration Year)
        "hgt", # (Height)
        "hcl", # (Hair Color)
        "ecl", # (Eye Color)
        "pid", # (Passport ID)
        "cid"  # (Country ID)
    }

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def is_valid(self):
        return self.key in self.valid_fields

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

    def field_is_required(self, key):
        return key in self.required_keys

    def add_field(self, key, value):
        field = Field(key, value)
        if field.is_valid() and self.field_is_required(key):
            self.fields[key] = value

    def is_valid(self):
        for key in self.required_keys:
            if self.fields[key] == None:
                return False
        print("Valid!")
        return True

# Code execution starts here
passports = []
passport = Passport()
for line in sys.stdin:
    if line == "\n":
        if passport.is_valid():
            passports.append(passport)
        passport = Passport()
    else:
        new_fields = line.strip().split(" ")
        for new_field in new_fields:
            key, value = new_field.split(":")
            passport.add_field(key, value)
 
