import os
import numpy

dynamic_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
inputs = None
with open(os.path.join(dynamic_location, 'input5.txt')) as f:
    inputs = f.read().splitlines()


# TODO: optimise the code; currently written in brute force way.
def calculate_lines(inputs, diagonal=False):
    points_collector = []
    common_points = []
    for input in inputs:
        input = input.split('->')
        first_part = tuple(int(i) for i in input[0].strip().split(','))
        second_part = tuple(int(i) for i in input[1].strip().split(','))
        if first_part[0] == second_part[0]:
            iter_range = (first_part[1], second_part[1]) if second_part[1] > first_part[1] else (second_part[1],
                                                                                                 first_part[1])
            for i in range(iter_range[0], iter_range[1] + 1):
                new_point = (first_part[0], i)
                if new_point not in points_collector:
                    points_collector.append(new_point)
                else:
                    if new_point not in common_points:
                        common_points.append(new_point)
        if first_part[1] == second_part[1]:
            iter_range = (first_part[0], second_part[0]) if second_part[0] > first_part[0] else (second_part[0],
                                                                                                 first_part[0])
            for i in range(iter_range[0], iter_range[1] + 1):
                new_point = (i, first_part[1])
                if new_point not in points_collector:
                    points_collector.append(new_point)
                else:
                    if new_point not in common_points:
                        common_points.append(new_point)
        #find out if two points are diagonally align via |𝑥1−𝑥2|=|𝑦1−𝑦2| or |𝑥1−y1|=|x2−𝑦2|
        if diagonal and abs(first_part[0] - first_part[1]) == abs(second_part[0] - second_part[1]) \
                or diagonal and abs(first_part[0] - second_part[0]) == abs(first_part[1] - second_part[1]):
            x_diff = first_part[0] - second_part[0]
            y_diff = first_part[1] - second_part[1]
            for i in range(abs(x_diff) + 1):
                new_point = None
                if new_point == (5, 5):
                    print(new_point)
                if x_diff < 0 and y_diff < 0:
                    new_point = (first_part[0] + i, first_part[1] + i)
                elif x_diff > 0 and y_diff < 0:
                    new_point = (first_part[0] - i, first_part[1] + i)
                elif x_diff > 0 and y_diff > 0:
                    new_point = (first_part[0] - i, first_part[1] - i)
                elif x_diff < 0 and y_diff > 0:
                    new_point = (first_part[0] + i, first_part[1] - i)
                if new_point not in points_collector:
                    points_collector.append(new_point)
                else:
                    if new_point not in common_points:
                        common_points.append(new_point)
    return common_points, points_collector


# part 1:
common_points, points_collector = calculate_lines(inputs, diagonal=False)
print("Part1: At how many points do at least two lines overlap?",
      len(common_points))

# part 2:
common_points, points_collector = calculate_lines(inputs, diagonal=True)
print("Part2: At how many points do at least two lines overlap?",
      len(common_points))
