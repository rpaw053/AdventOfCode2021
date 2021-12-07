import os
import copy

dynamic_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputs = None
with open(os.path.join(dynamic_location, 'input7.txt')) as f:
    horizontal_positions = f.read().split(",")

inputs = [int(input) for input in horizontal_positions]

difference = []
for hp in inputs:
    temp_difference = []
    for i, val in enumerate(inputs):
        temp_difference.append(abs(hp-inputs[i]))
    if sum(temp_difference) < sum(difference) or not difference:
        difference = temp_difference

print("Part1: How much fuel must they spend to align to that position?",
      sum(difference))

# part 2:
difference = []
max = max(inputs)
for hp in range(max+1):
    temp_difference = []
    for i, val in enumerate(inputs):
        diff = abs(hp-inputs[i])
        c = 0
        while diff > 0:
            c = c + diff
            diff = diff - 1
        temp_difference.append(c)
    if sum(temp_difference) < sum(difference) or not difference:
        difference = temp_difference

print("Part2: How much fuel must they spend to align to that position?",
      sum(difference))