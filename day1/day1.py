import os

dynamic_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
depth_measurements = 0
with open(os.path.join(dynamic_location, 'input1.txt')) as f:
    depth_measurements = [int(depth) for depth in f.read().splitlines()]


def count_larger_than_previos(depth_measurements):
    increased_count = 0
    previous_depth = 0
    for depth in depth_measurements:
        if previous_depth and depth > previous_depth:
            increased_count = increased_count + 1
        previous_depth = depth
    return increased_count


# part 1:
increased_count = count_larger_than_previos(depth_measurements)
print("Part1: How many measurements are larger than the previous measurement: ", increased_count)

# part 2:
sliding_window = []
for i, val in enumerate(depth_measurements):
    try:
        sliding_window.append(depth_measurements[i] +
                              depth_measurements[i + 1] +
                              depth_measurements[i + 2])
    except IndexError as ie:
        # Stop when there aren't enough measurements left to create a new three-measurement sum
        break
    except Exception as e:
        sliding_window = []
        print("Exception found:", e)

increased_count = count_larger_than_previos(sliding_window)
print("Part2: How many sums are larger than the previous sum?: ", increased_count)
