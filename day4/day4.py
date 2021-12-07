import os
import numpy

dynamic_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputs = None
with open(os.path.join(dynamic_location, 'input4.txt')) as f:
    inputs = f.read().splitlines()

random_numbers = inputs.pop(0).split(",")

inputs = [i.split() for i in inputs if '' != i]
number_of_boards = len(inputs) / 5

formatted_inputs = numpy.array_split(inputs, number_of_boards)

# TODO: optimise the code; currently written in brute force way.


def squid_bingo(random_numbers, formatted_inputs):
    winning_bracket = None
    winning_number = None
    bracket_number = None
    break_ = False

    for ra in random_numbers:
        j = 0
        for fi in formatted_inputs:
            k = 0
            for f in fi:
                i = 0
                while i < 5:
                    if ra == f[i]:
                        formatted_inputs[j][k][i] = "*"
                        if all(x == '*' for x in formatted_inputs[j][k]):
                            winning_bracket = formatted_inputs[j]
                            winning_number = ra
                            bracket_number = j
                            break_ = True
                            break
                        for gg in range(5):
                            if all(t == '*' for x in formatted_inputs[j] for t in x[gg]):
                                winning_bracket = formatted_inputs[j]
                                winning_number = ra
                                bracket_number = j
                                break_ = True
                                break
                        if break_:
                            break
                    i = i + 1
                k = k + 1
                if break_:
                    break
            j = j + 1
            if break_:
                break
        if break_:
            break
    return winning_bracket, winning_number, bracket_number


winning_bracket, winning_number, bracket_number = squid_bingo(random_numbers, formatted_inputs)
winning_bracket_sum = sum([int(w) for wi in winning_bracket for w in wi if w != '*'])

# part 1:
print("Part1: What will your final score be if you choose that board? ",
      winning_bracket_sum * int(winning_number))

formatted_inputs = numpy.array_split(inputs, number_of_boards)

# part 2:
while number_of_boards > 0:
    winning_bracket, winning_number, bracket_number = squid_bingo(random_numbers, formatted_inputs)
    del formatted_inputs[bracket_number]
    number_of_boards = number_of_boards - 1

winning_bracket_sum = sum([int(w) for wi in winning_bracket for w in wi if w != '*'])

print("Part2: Once it wins, what would its final score be? ",
      winning_bracket_sum * int(winning_number))
