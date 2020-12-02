# day 13
import Intcode
EXTEND = 1000

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

	#compute result part 1
	part1, _ = Intcode.compute_result(numbers)
	print("\nPart1:  " + str(part1))

	#compute result part 2
	numbers_part2[0] = 2
	_, part2 = Intcode.compute_result(numbers_part2)
	print("Part2:  " + str(part2) + "\n")
