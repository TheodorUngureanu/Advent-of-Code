#day 3

global_path = {}		# better use dictionary for searching
crossover = []			# list for position where wire intersect
number_moves = {}		# for moves counter in part2

# number means wire number
# number = 0  (wire 1)
# number = 1  (wire 2)
def compute_road(path, number):
	curent = [0,0]	# starting position in grid
	moves = 0	    # reset moves counter

	for step in path:
		direction, value = step[0], int(step[1:])
		x, y = directions[direction]

		for _ in range(value):
			curent[0] += x
			curent[1] += y
			pair = tuple(curent)
			moves += 1

			if number == 1:
				if pair in global_path:
					crossover.append(pair)
					number_moves[pair] = moves + global_path[pair]
			else:
				global_path[pair] = moves


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()

	# dictionary with direction possible
	directions = {"R":(0,1),"L":(0,-1),"U":(1,0),"D":(-1,0)}

	# generating wire paths/moves
	wire1 = lines[0].split(',')
	wire2 = lines[1].split(',')

	compute_road(wire1, 0)
	compute_road(wire2, 1)

	# Results
	print("\nPart 1:  " + str(min(abs(p[0]) + abs(p[1]) for p in crossover)))
	print("Part 2:  " + str(min(number_moves.items(), key=lambda x: x[1])) + "\n")
