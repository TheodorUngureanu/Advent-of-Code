#day 6

# dictionary --> key: child  value: parent
dictionary = {}

def compute_path(planet):
	path = []

	# compute the entire path till root
	while True:
		next_planet = dictionary.get(planet)

		if not next_planet:		# this means the root
			break
		else:					# move to next planet
			planet = next_planet
			path.append(planet)

	return path


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()

	# parse the input
	for line in lines:
		parent, child = line.split(')')
		dictionary[child] = parent

	# part 1
	number = 0
	for planet in dictionary:
		number += len(compute_path(planet))
	print("\nPart 1:  " + str(number))

	# part 2
	# uniwqe planets from you to com
	path_YOU = set(compute_path("YOU"))
	path_SAN = set(compute_path("SAN"))
	# unique orbit that are not common
	print("Part 2:  " + str(len(path_YOU ^ path_SAN)) + "\n")
