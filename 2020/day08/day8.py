#day 8

def run(program):
	i = acc = 0
	occurances = dict.fromkeys(range(len(program)), 0)

	while True:
		# print(acc, i)
		if program[i][0] == "nop":
			if occurances[i] >= 1:
				return acc, i, False
			else:
				occurances[i] += 1
				i += 1
		
		elif program[i][0] == "acc":
				if occurances[i] >=1:
					return acc, i, False
				else:
					acc += program[i][1]
					occurances[i] += 1
					i += 1

		else:
			if occurances[i] >= 1 :
				return acc, i, False
			else:
				occurances[i] += 1
				i += program[i][1]
		
		if i >= len(program):
			return acc, i, True


def computePart2(program):
	for i in range(len(program)):
		if program[i][0] == "nop" or program[i][0] == "jmp":

			if program[i][0] == "jmp":
				program[i][0] = "nop"
			else:
				program[i][0] = "jmp"

			accumulator, finishIndex, finished = run(program)

			if finished:
				return accumulator, i, finished
			
			else:
				if program[i][0] == "jmp":
					program[i][0] = "nop"
				else:
					program[i][0] = "jmp"


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)
	
	program = []
	for line in lines:
		aux = line.split(" ")
		program.append([aux[0], int(aux[1])])
	
	# print(program)
	print("Part1: " + str(run(program)[0]))
	print("Part2: " + str(computePart2(program)[0]))