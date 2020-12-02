# day 8
# run using python 3
import sys

LINE = 6
COLUMN = 25

if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()

	# all numbers
	numbers = list(lines[0])

	layers = {}
	# for all layers
	size = int(len(numbers) / LINE / COLUMN)
	for i in range(size):
		layers[i] = numbers[i * LINE * COLUMN : (i + 1) * LINE * COLUMN]

	#finding layer with fewest 0 digits
	max_digit0_layer = None
	max_digit0_counter = sys.maxsize
	for layer in layers:
		counter = layers[layer].count('0')
		if counter < max_digit0_counter:
			max_digit0_layer = layer
			max_digit0_counter = counter

	# Results
	print("\nPart 1:  " + str(layers[max_digit0_layer].count('1')*
							  layers[max_digit0_layer].count('2')))

	# part2
	# number of layers
	layer_number = len(layers)

	# define a matrix of size LINE * COLUMN
	matrix = ['.'] * (LINE * COLUMN)		# default for transparent

	# for every layer put a simbol in matrix respecting rules (transparency, black, white)
	for layer in layers:
		for i in range(LINE):
			for j in range(COLUMN):
				# insert space for black
				if layers[layer][i * COLUMN + j] == '0' and matrix[i *COLUMN + j] == '.':
					matrix[i * COLUMN + j] = ' '
				# insert * for white
				if layers[layer][i * COLUMN + j] == '1' and matrix[i *COLUMN + j] == '.':
					matrix[i * COLUMN + j] = '*'

	print("\nPart 2:  ")
	for i in range(LINE):
		for j in range(COLUMN):
			print(matrix[i * COLUMN + j], end = '')
		print('')
