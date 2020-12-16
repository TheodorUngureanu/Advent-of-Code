#day 15

def computePart1(lines, turns):
	numbers = list(map(int, lines.split(',')))

	memory = {}

	# store turn for given numbers but last
	for number in numbers[:-1]:
		memory[number] = numbers.index(number) + 1

	lastNumberSpoken = numbers[-1]

	for turn in range(len(numbers), turns):
		if memory.get(lastNumberSpoken, None) != None:
			aux = lastNumberSpoken
			lastNumberSpoken = turn - memory[lastNumberSpoken]
			memory[aux] = turn

		else:
			memory[lastNumberSpoken] = turn
			lastNumberSpoken = 0

	return lastNumberSpoken
	

if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)
	
	print("Part1: " + str(computePart1(lines[0], 2020)))
	print("Part2: " + str(computePart1(lines[0], 30000000)))