# day 16
from operator import mul
STEPS = 100

def compute_phase(numbers):
	new_array = []
	for i in range(len(numbers)):
		# base pattern (make it same lenght as input)
		base_pattern = [0] * (i+1) + [1] * (i + 1) + [0] * (i+1) + [-1] * (i + 1)
		base_pattern = base_pattern * (len(numbers) / len(base_pattern) + 1)
		base_pattern = base_pattern[1:len(numbers)+1]
		#compute result
		number = abs(sum(map(mul, numbers, base_pattern)))
		new_array.append(number%10)
	return new_array


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()

	# make a list of integers with every digit
	numbers = list(lines[0])
	numbers = map(int, numbers)
	numbers_part2 = numbers[:]

	# compute part 1
	for _ in range(STEPS):
		numbers = compute_phase(numbers)
	output = str(''.join(str(x) for x in numbers))
	print("\nPart1:  " + output[0:8])

	# compute part 2
	# number of digits to skip
	offset = int("".join(map(str, numbers_part2[0:7])))
	numbers_part2 = numbers_part2 * 10000
	numbers_part2 = numbers_part2[offset:]

	# new way of thinking
	# we can see the calculus as a triangular superior matrix
	# last element remain the same
	# n-1 element is (elem(n) + elem(n-1))%10
	# n-2 element is (elem(n-1) + elem(n-2))%10
	# the key is that we should start backwards
	for _ in range(STEPS):
		for i in range(len(numbers_part2) - 1, 0, -1): # start from the end
			numbers_part2[i-1] = (numbers_part2[i - 1] + numbers_part2[i]) % 10
	output = str(''.join(str(x) for x in numbers_part2))
	print("Part2:  " + str(output[0:8]) + "\n")
