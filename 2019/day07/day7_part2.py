#day 7
from itertools import permutations

def get_mode(opcode, number):
	number = number / 100	# removing the opcode
	mode_list = []			# list with parameters modes

	#modes for opcode 1,2,7,8 (3 params, 3 modes)
	if opcode in [1, 2, 7, 8]:
		for _ in range(3):
			mode_list.append(number % 10)
			number /=10

	# moodes for opcode 3 and opcode 4 (1 params, 1 mode)
	elif opcode in [3, 4]:
		mode_list.append(number % 10)

	# moodes for opcode 5 and opcode 6(3 params, 3 modes)
	elif opcode in [5, 6]:
		for _ in range(2):
			mode_list.append(number % 10)
			number /=10

	return mode_list


def compute_result(numbers, input_intruction, i_position):
	#loop
	i = i_position

	while (i < len(numbers)):
		opcode = numbers[i]
		if(opcode > 100):
			opcode = opcode % 100

		#get mode for opcode parameters
		mode_list = get_mode(opcode, numbers[i])

		if (opcode == 99):
			return numbers[:], None, i

		elif (opcode == 1):
			op1 = numbers[i + 1]
			if mode_list[0] == 0:
				op1 = numbers[op1]

			op2 = numbers[i + 2]
			if mode_list[1] == 0:
				op2 = numbers[op2]

			numbers[numbers[i + 3]] = op1 + op2
			i += 4


		elif (opcode == 2):
			op1 = numbers[i + 1]
			if mode_list[0] == 0:
				op1 = numbers[op1]

			op2 = numbers[i + 2]
			if mode_list[1] == 0:
				op2 = numbers[op2]

			numbers[numbers[i + 3]] = op1 * op2
			i += 4


		elif (opcode == 3):
			op1 = numbers[i + 1]
			# for each input reading take the first element of array
			numbers[op1] = input_intruction[0]
			input_intruction.pop(0)
			i += 2


		elif (opcode == 4):
			op1 = numbers[i + 1]
			if mode_list[0] == 0:
				op1 = numbers[op1]
			i += 2
			return numbers[:], op1, i


		elif (opcode == 5):
			op1 = numbers[i + 1]
			if mode_list[0] == 0:
				op1 = numbers[op1]

			op2 = numbers[i + 2]
			if mode_list[1] == 0:
				op2 = numbers[op2]

			if op1 != 0:
				i = op2
			else:
				i += 3


		elif (opcode == 6):
			op1 = numbers[i + 1]
			if mode_list[0] == 0:
				op1 = numbers[op1]

			op2 = numbers[i + 2]
			if mode_list[1] == 0:
				op2 = numbers[op2]

			if op1 == 0:
				i = op2
			else:
				i += 3


		elif (opcode == 7):
			op1 = numbers[i + 1]
			if mode_list[0] == 0:
				op1 = numbers[op1]

			op2 = numbers[i + 2]
			if mode_list[1] == 0:
				op2 = numbers[op2]

			if op1 < op2:
				numbers[numbers[i + 3]] = 1
			else:
				numbers[numbers[i + 3]] = 0
			i += 4


		elif (opcode == 8):
			op1 = numbers[i + 1]
			if mode_list[0] == 0:
				op1 = numbers[op1]

			op2 = numbers[i + 2]
			if mode_list[1] == 0:
				op2 = numbers[op2]

			if op1 == op2:
				numbers[numbers[i + 3]] = 1
			else:
				numbers[numbers[i + 3]] = 0
			i += 4

		else:
			print("invalid opcode")
			return


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()

	#split into numbers
	numbers = lines[0].split(',')

	#convert to int
	numbers = [int(i) for i in numbers]

	#compute result
	max_value = 0
	max_permutation = None
	perm = permutations([5, 6, 7, 8, 9])
	# for every permutation find the output value
	for p in perm:
		# position for i in every numbers array
		i_position_array = [0] * len(p)
		# queue for input instructions for every amplifier
		queue = [[p[i]] for i in range(len(p))]
		queue[0].append(0)
		# numbers array for each amplifier
		numbers_amplifier = [numbers[:]] * len(p)
		# values for amplifier E
		value_E = 0

		run = True
		while run:
			for i in range(len(p)):
				numbers_amplifier[i], output, new_i_pos = compute_result(numbers_amplifier[i], queue[i], i_position_array[i])
				if output is None:
					if value_E > max_value:
						max_value = value_E
						max_permutation = p
					run = False
					break

				#update data
				i_position_array[i] = new_i_pos
				value_E = output
				queue[(i + 1) % len(queue)].append(output)


	print("\nPart 2:  ")
	print("	Permutation: " + str(max_permutation))
	print("	Value: " + str(max_value) + "\n")
