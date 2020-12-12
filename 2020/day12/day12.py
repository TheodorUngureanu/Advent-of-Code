#day 12

DIRECTIONS = {'N':((0,1), 0), 'E':((1,0), 1), 'S':((0,-1), 2), 'W':((-1,0), 3)}
COORDINATES = {0: 'N', 1: 'E', 2: 'S', 3: 'W'}

def turn(old_direction, action, value):
    if action == 'R':
        compas = COORDINATES[(old_direction[1] + value / 90) % 4]
    
    elif action == 'L':
        compas = COORDINATES[(old_direction[1] + 4 - value / 90) % 4]

    return DIRECTIONS[compas]


def computePart1(lines):
    position = {'x': 0, 'y':0}
    direction = DIRECTIONS['E']

    for line in lines:
        action = line[0]
        value = int(line[1:])

        if action == 'N':
            position['y'] += value

        elif action == 'S':
            position['y'] -= value

        elif action == 'W':
            position['x'] -= value

        elif action == 'E':
            position['x'] += value

        elif action == 'L':
            direction = turn(direction, action, value)

        elif action == 'R':
            direction = turn(direction, action, value)

        elif action == 'F':
            position['x'] += direction[0][0] * value
            position['y'] += direction[0][1] * value

    return abs(position['x']) +  abs(position['y']), position['x'], position['y']


def rotate(old_position, action, value):
    new_position = {'x': 0, 'y':0}

    aux = 1 if action == 'R' else -1

    if value == 90:
        new_position['x'] = aux * old_position['y']
        new_position['y'] = -aux * old_position['x']

    elif value == 180:
        new_position['x'] = -old_position['x']
        new_position['y'] = -old_position['y']

    elif value == 270:
        new_position['x'] = -aux * old_position['y']
        new_position['y'] = aux * old_position['x']

    return new_position


def computePart2(lines):
    waypoint_position = {'x': 10, 'y':1}
    ship_position = {'x': 0, 'y':0}

    for line in lines:
        action = line[0]
        value = int(line[1:])

        if action == 'N':
            waypoint_position['y'] += value

        elif action == 'S':
            waypoint_position['y'] -= value

        elif action == 'W':
            waypoint_position['x'] -= value

        elif action == 'E':
            waypoint_position['x'] += value

        elif action in ['L', 'R']:
            waypoint_position = rotate(waypoint_position, action, value)

        elif action == 'F':
            ship_position['x'] += waypoint_position['x'] * value
            ship_position['y'] += waypoint_position['y'] * value

    return abs(ship_position['x']) +  abs(ship_position['y']), ship_position['x'], ship_position['y']


if __name__ == "__main__":
    with open("input", 'r') as input:
        lines = input.read().splitlines()
        # print(lines)
    
    print("Part1: " + str(computePart1(lines)[0]))
    print("Part2: " + str(computePart2(lines)[0]))