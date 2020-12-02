from __future__ import print_function
import Intcode
# day 17

EXTEND = 2000

# prints the path matrix
def print_path(output):
	size_line = -1
	size_col = -1
	col = True
	for elem in output:
		if col:
			size_col += 1
		if elem == 35:
			print("#", end = '')
		elif elem == 46:
			print(".", end = '')
		elif elem == 10:
			size_line += 1
			col = False
			print("\n", end = '')
		else:
			if int(elem) > 127:
				print("\nPart2:  " + str(elem))
			else:
				print(chr(int(elem)), end = '')
			# print(elem, end = '')
	return size_line, size_col

# construct a matrix with 1 on the path and 0 otherwise
def compute_matrix(output, lines, cols):
	matrix = [[0 for j in range(cols)] for i in range(lines)]
	i = 0
	while i < len(output):
		if output[i] == 35:
			matrix[i / cols][i % cols] += 1
			i += 1
		elif output[i] == 46:
			matrix[i / cols][i % cols] = 0
			i += 1
		elif output[i] == 10:
			output.remove(output[i])
		else:
			matrix[i / cols][i % cols] += 1
			i += 1
	return matrix

# find position in the matrix where there is an intersection in path
def find_intersections(matrix, lines, cols):
	intersections = []
	for i in range(lines):
		for j in range(cols):
			# check if there is cross
			if i < lines-1 and i > 1 and j < cols-1 and j > 1:
				if (matrix[i-1][j] == 1 and matrix[i+1][j] == 1 and
					matrix[i][j-1] == 1 and matrix[i][j+1] == 1 and
					matrix[i][j] == 1):
					intersections.append((i, j))
	return intersections

# calculate result for part 1
def compute_part1(intersections):
	res = 0
	for elem in intersections[:]:
		res += elem[0] * elem[1]
	return res

# compute part2 input. Look at the map from part 1 and try to find a pattern
def compute_input_part2():
	string = ('A,B,A,B,A,C,B,C,A,C\n'
			  'L,10,L,12,R,6\n'
			  'R,10,L,4,L,4,L,12\n'
			  'L,10,R,10,R,6,L,4\n'
			  'n\n')
	x = list(map(ord, list(string)))
	return x


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()

	#split into numbers
	numbers = lines[0].split(',')

	#convert to int
	numbers = [int(i) for i in numbers]

	#extend list
	numbers.extend([0] * EXTEND)

	#make a copy for part2
	numbers_part2 = numbers[:]

	#compute part1
	output = Intcode.compute_result(numbers, None)
	lines, cols = print_path(output)
	matrix = compute_matrix(output, lines, cols)
	intersections = find_intersections(matrix, lines, cols)
	part1 = compute_part1(intersections)
	print("\nPart1:  " + str(part1) + "\n")

	#compute part2
	numbers_part2[0] = 2
	input_list = compute_input_part2()
	output = Intcode.compute_result(numbers_part2, input_list)
	lines, cols = print_path(output)
