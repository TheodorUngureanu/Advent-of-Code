#day 14
from itertools import product
from more_itertools import locate


def computePart1(lines):
	memory = {}
	mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

	for line in lines:
		aux = line.split(' = ')
		if aux[0] == 'mask':
			mask = aux[1]
		
		else:
			memory_adress = int(aux[0][4:-1])
			value = int(aux[1])
			orMask = int(mask.replace('X', '0'), 2)
			andMask = int(mask.replace('X', '1'), 2)
			memory[memory_adress] = (value | orMask) & andMask
			
	return sum(memory.values())


def createMasks(X_indices, mask):
	# all posible combination of 1 and 0 for X occurances
	X_values = list(product(range(2), repeat=len(X_indices)))
	masks = []

	# for each possible combination
	for combination in X_values:
		new_mask = list(mask[:])

		# for each value of combination
		for i in range(0, len(combination)):
			new_mask[X_indices[i]] = str(combination[i])
		
		number = ''.join(new_mask)
		masks.append(int(number, 2))
	
	return masks


def computePart2(lines):
	memory = {}
	masks = []
	given_mask = None

	for line in lines:
		aux = line.split(' = ')
		if aux[0] == 'mask':
			given_mask = int(''.join('0' if letter in ['X', '1'] else '1' for letter in aux[1]), 2)
			X_indices = list(locate(list(aux[1]), lambda x: x == 'X'))
			masks = createMasks(X_indices, aux[1])
		
		else:
			memory_adress = int(aux[0][4:-1])
			value = int(aux[1])

			for mask in masks:
				memory[given_mask & memory_adress | mask] = value
			
	return sum(memory.values())


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)
	
	print("Part1: " + str(computePart1(lines)))	
	print("Part2: " + str(computePart2(lines)))	