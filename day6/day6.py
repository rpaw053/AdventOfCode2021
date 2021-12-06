import os
import copy

dynamic_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputs = None
with open(os.path.join(dynamic_location, 'input6.txt')) as f:
    inputs = f.read().split(",")


def calculate_fish(inputs, days):
    today = 0
    while today != days:

        c = copy.deepcopy(inputs)
        for i, val in enumerate(c):
            if val != 0:
                inputs[i] = inputs[i] - 1
            else:
                inputs[i] = 6
                inputs.append(8)

        today = today + 1
    return inputs

inputs = [int(input) for input in inputs]

print("Part1: How many lanternfish would there be after 80 days?",
      len(calculate_fish(inputs, 80)))

print("Part2: How many lanternfish would there be after 256 days?",
      len(calculate_fish(inputs, 176)))
