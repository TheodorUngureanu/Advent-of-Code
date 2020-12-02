# day 10
from math import atan2, hypot, pi
import operator

# calculate angle of 2 points
def angle(a, b):
	out = atan2(b[0] - a[0], a[1] - b[1])
	# to change order to clockwise
	if out > pi/2.0:
		out -= 2 * pi
	return out


# return number of point visible from a
def visible_from_a(asteroids, a):
	# set because we need only point that are visible
	unique = set()
	for i in asteroids:
		if i != a:
			unique.add(angle(a, i))
	return len(unique), unique


# return maximum number of point visible from one asteroid
def compute_part1(asteroids):
	# containt a tuple (first: asteroid coordinates; second: visible_from_a)
	visible_from_asteroids = []
	for a in asteroids:
		visible_from_asteroids.append((a, visible_from_a(asteroids, a)))
	return max(visible_from_asteroids, key=operator.itemgetter(1))


# function to retrun a list with angle from asteroid and distance
def angle_and_distance(asteroids, a):
	out = []
	for ast in asteroids:
		radian_angle = angle(ast, a)
		distance = hypot(ast[0] - a[0], ast[1] - a[1])
		out.append((radian_angle, distance, ast))
	return out


def compute_new_list(to_sort):
	# creating a new list that contains only first cicle points to be deleted
	new_list = []
	new_list.append(to_sort[0])
	# to_sort.remove(to_sort[0])

	for i in range(len(to_sort)):
		if i >= 1:
			if to_sort[i][0] != to_sort[i - 1][0]:
				new_list.append(to_sort[i])
				# to_sort.remove(to_sort[i])
	return new_list


def compute_part2(asteroids):
	coord, number = compute_part1(asteroids)
	# remove asteroid found in part1
	asteroids.remove(coord)
	out = angle_and_distance(asteroids, coord)
	# sort first angle and after distance
	to_sort = list(reversed(sorted(out,  key=lambda x: (x[0], -x[1]))))
	# new list for clockwise
	out = compute_new_list(to_sort)
	winner = out[199][2]
	return winner[0], winner[1]


if __name__ == "__main__":

	with open("input", 'r') as input:
		lines = input.read().splitlines()

	asteroids = []
	for i in range(len(lines)):
		for j in range(len(lines[0])):
			if lines[i][j] == '#':
				asteroids.append((i, j))

	# part 1
	coord, number = compute_part1(asteroids)
	print("\nPart1:\n	x: " +  str(coord[0]) + " y: " + str(coord[1]))
	print("	number: " + str(number[0]))

	# part2
	part2 = compute_part2(asteroids)
	print("Part2:\n	x: " +  str(part2[0]) + " y: " + str(part2[1]))
	print("	result: " + str(part2[0] * 100 + part2[1]) + "\n")
	print("	result v2: " + str(part2[1] * 100 + part2[0]) + "\n")
