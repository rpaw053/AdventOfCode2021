import os

dynamic_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputs = None
with open(os.path.join(dynamic_location, 'input3.txt')) as f:
    inputs = f.read().splitlines()


def count_gamma_epsilon(inputs):
    gamma = ''
    epsilon = ''
    iter = 0
    len_of_input = len(inputs[0])
    while iter < len_of_input:
        number_of_zeros = 0
        number_of_ones = 0
        for input in inputs:
            bit = input[iter]
            if bit == "0":
                number_of_zeros = number_of_zeros + 1
            elif bit == "1":
                number_of_ones = number_of_ones + 1
        if number_of_zeros > number_of_ones:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
        else:
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        iter = iter + 1
    return int(gamma, 2), int(epsilon, 2)


def count_oxy_co2(inputs, element):
    iter = 0
    len_of_input = len(inputs[0])
    while len(inputs) > 1:
        number_of_zeros = 0
        number_of_ones = 0
        zero_list = []
        one_list = []
        for input in inputs:
            bit = input[iter]
            if bit == "0":
                number_of_zeros = number_of_zeros + 1
                zero_list.append(input)
            elif bit == "1":
                number_of_ones = number_of_ones + 1
                one_list.append(input)
        if number_of_zeros > number_of_ones:
            if element == 'oxy':
                inputs = zero_list
            else:
                inputs = one_list
        elif number_of_zeros < number_of_ones:
            if element == 'oxy':
                inputs = one_list
            else:
                inputs = zero_list
        else:
            if element == 'oxy':
                inputs = one_list
            else:
                inputs = zero_list
        iter = iter + 1
    return int(inputs[0], 2)


# part 1:
gamma, epsilon = count_gamma_epsilon(inputs)
print("Part1: What is the power consumption of the submarine? ",
      gamma * epsilon)

# part 2:
oxy = count_oxy_co2(inputs, element='oxy')
co2 = count_oxy_co2(inputs, element='co2')
print("Part2: What is the life support rating of the submarine? ",
      oxy * co2)
