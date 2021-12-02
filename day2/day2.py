import os

dynamic_location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
directions = None
with open(os.path.join(dynamic_location, 'input2.txt')) as f:
    directions = f.read().splitlines()


def count_horizontal_depth(directions):
    horizontal_position = 0
    depth = 0
    for direction in directions:
        direction, value = direction.split(' ')
        if 'forward' == direction:
            horizontal_position = horizontal_position + int(value)
        elif 'down' == direction:
            depth = depth + int(value)
        elif 'up' == direction:
            depth = depth - int(value)
    return horizontal_position, depth


def count_horizontal_depth_aim(directions):
    horizontal_position = 0
    depth = 0
    aim = 0
    for direction in directions:
        direction, value = direction.split(' ')
        if 'forward' == direction:
            horizontal_position = horizontal_position + int(value)
            depth = depth + aim * int(value)
        elif 'down' == direction:
            aim = aim + int(value)
        elif 'up' == direction:
            aim = aim - int(value)
    return horizontal_position, depth


# part 1:
horizontal_position, depth = count_horizontal_depth(directions)
print("Part1: What do you get if you multiply your final horizontal position by your final depth? ",
      horizontal_position * depth)

# part 2:
horizontal_position, depth = count_horizontal_depth_aim(directions)
print("Part2: What do you get if you multiply your final horizontal position by your final depth? ",
      horizontal_position * depth)