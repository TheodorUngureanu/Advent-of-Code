#day 2
import copy

OUTPUT = 19690720

def compute_result(numbers):
	#loop
	i = 0
	while (i < len(numbers)):
		# print("valoarea: " + str(numbers[i]) + " valoare i: " + str(i))
		if (numbers[i] == 99):
			break

		elif (numbers[i] == 1):
			op1 = numbers[i + 1]
			op2 = numbers[i + 2]
			res = numbers[i + 3]
			numbers[res] = numbers[op1] + numbers[op2]
			i += 4

		elif (numbers[i] == 2):
			op1 = numbers[i + 1]
			op2 = numbers[i + 2]
			res = numbers[i + 3]
			numbers[res] = numbers[op1] * numbers[op2]
			i += 4

		else:
			print("invalid opcode")
			break
	return numbers[0]


if __name__ == "__main__":


	with open("input", 'r') as input:
		lines = input.read().splitlines()
		#print(lines)

	#split into numbers
	numbers = lines[0].split(',')
	# print("lungime: " + str(len(numbers)))

	#replacements
	numbers[1] = 12
	numbers[2] = 2

	#convert to int
	numbers = [int(i) for i in numbers]

	#backup copy
	backup = copy.copy(numbers)
	#print(numbers)

	#compute part1
	out = compute_result(numbers)

	print("\nPart1:\n  " + str(out) + "\n")

	for i in range(0,100):
		for j in range(0, 100):
			#restore copy
			numbers = copy.copy(backup)
			#update noun and verb
			numbers[1] = i
			numbers[2] = j
			out = compute_result(numbers)
			if (out == OUTPUT):
				print("Part2:\n  Noun: " +  str(i) + "\n  Verb: " + str(j) + "\n  100 * noun + verb: " + str(100 * i + j) + "\n")
