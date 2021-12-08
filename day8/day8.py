import os
import copy

dynamic_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputs = None
with open(os.path.join(dynamic_location, 'input8.txt')) as f:
    inputs = f.read().splitlines()


unique = 0
for input in inputs:
    signal_patterns, digits = input.split("|")
    digits = digits.strip().split()
    for dg in digits:
        if len(dg) in [2, 4, 3, 7]:
            unique = unique + 1

print("Part1: how many times do digits 1, 4, 7, or 8 appear?",
      unique)


unique = 0
for input in inputs:
    signal_patterns, digits = input.split("|")
    signal_patterns = signal_patterns.strip().split()
    for signal_pattern in signal_patterns:
        if len(signal_pattern) == 2:
            print("1:", signal_pattern)
        elif len(signal_pattern) == 4:
            print("4:", signal_pattern)
        elif len(signal_pattern) == 3:
            print("7:", signal_pattern)
        elif len(signal_pattern) == 7:
            print("8:", signal_pattern)

#TODO: part 2
