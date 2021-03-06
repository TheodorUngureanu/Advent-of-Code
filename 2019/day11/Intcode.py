import day11

def get_mode(opcode, number):
	number = number / 100	# removing the opcode
	mode_list = []			# list with parameters modes

	#modes for opcode 1,2,5,6,7,8 (3 params, 3 modes)
	if opcode in [1, 2, 5, 6, 7, 8]:
		for i in range(3):
			mode_list.append(number % 10)
			number /=10

	# moodes for opcode 3 and opcode 4 (1 params, 1 mode)
	elif opcode in [3, 4, 9]:
		mode_list.append(number % 10)
	return mode_list

# get value for future parameter
def get_value(mode, numbers, i, rel_base):
	if mode == 0:
		value = numbers[numbers[i]]
	elif mode == 1:
		value = numbers[i]
	elif mode == 2:
		value = numbers[numbers[i] + rel_base]
	return value

# get position where result will be stored later
def get_position(mode, numbers, i, rel_base):
	if mode == 0:
		value = numbers[i]
	elif mode == 2:
		value = numbers[i] + rel_base
	return value


def compute_result(numbers, robo, color):
	# count nr of out
	out_nr = 0
	rel_base = 0
	#loop
	i = 0
	while (i < len(numbers)):
		opcode = numbers[i]
		if(opcode > 99):
			opcode = opcode % 100

		#get mode for opcode parameters
		mode_list = get_mode(opcode, numbers[i])

		if (opcode == 99):
			return robo

		elif (opcode == 1):
			op1 = get_value(mode_list[0], numbers, i + 1, rel_base)
			op2 = get_value(mode_list[1], numbers, i + 2, rel_base)
			op3 = get_position(mode_list[2], numbers, i + 3, rel_base)
			numbers[op3] = op1 + op2
			i += 4


		elif (opcode == 2):
			op1 = get_value(mode_list[0], numbers, i + 1, rel_base)
			op2 = get_value(mode_list[1], numbers, i + 2, rel_base)
			op3 = get_position(mode_list[2], numbers, i + 3, rel_base)
			numbers[op3] = op1 * op2
			i += 4


		elif (opcode == 3):
			op1 = get_position(mode_list[0], numbers, i + 1, rel_base)
			if (robo.pos[0], robo.pos[1]) not in robo.painted:
				numbers[op1] = color   # 0 for part 1 ; 1 for part 2
			else:
				numbers[op1] = robo.painted[(robo.pos[0], robo.pos[1])]
			i += 2


		elif (opcode == 4):
			op1 = get_value(mode_list[0], numbers, i + 1, rel_base)
			# print("OUTPUT: " + str(op1))
			if out_nr == 1:
				robo.move(op1)
				out_nr = 0

			elif out_nr == 0:
				robo.paint(op1)
				out_nr += 1
			i += 2


		elif (opcode == 5):
			op1 = get_value(mode_list[0], numbers, i + 1, rel_base)
			op2 = get_value(mode_list[1], numbers, i + 2, rel_base)
			if op1 != 0:
				i = op2
			else:
				i += 3


		elif (opcode == 6):
			op1 = get_value(mode_list[0], numbers, i + 1, rel_base)
			op2 = get_value(mode_list[1], numbers, i + 2, rel_base)
			if op1 == 0:
				i = op2
			else:
				i += 3


		elif (opcode == 7):
			op1 = get_value(mode_list[0], numbers, i + 1, rel_base)
			op2 = get_value(mode_list[1], numbers, i + 2, rel_base)
			op3 = get_position(mode_list[2], numbers, i + 3, rel_base)
			if op1 < op2:
				numbers[op3] = 1
			else:
				numbers[op3] = 0
			i += 4


		elif (opcode == 8):
			op1 = get_value(mode_list[0], numbers, i + 1, rel_base)
			op2 = get_value(mode_list[1], numbers, i + 2, rel_base)
			op3 = get_position(mode_list[2], numbers, i + 3, rel_base)
			if op1 == op2:
				numbers[op3] = 1
			else:
				numbers[op3] = 0
			i += 4


		elif (opcode == 9):
			op1 = get_value(mode_list[0], numbers, i + 1, rel_base)
			rel_base += op1
			i += 2

		else:
			print("invalid opcode")
			return None
