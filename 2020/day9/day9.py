#day 9

def check(numbers, sumNumber):
	for i in range(0, len(numbers) - 1):
		for j in range(i+1, len(numbers)):
			if numbers[i] + numbers[j] == sumNumber:
				return True
	return False


def computePart1(numbers, previousMagicNumber):
	number = None
	for i in range(previousMagicNumber, len(numbers)):
		if not check(numbers[i - previousMagicNumber : i], numbers[i]):
			number = numbers[i]
			break
	return number


def computePart2(numbers, part1):
	for i in range(len(numbers)): 
		currentSum = numbers[i] 

		# finding subArrays
		j = i + 1
		while j <= len(numbers): 
			if currentSum == part1: 
				# the subArray sum is between i and j 
				return max(numbers[i:j-1]), min(numbers[i:j-1]), max(numbers[i:j-1]) + min(numbers[i:j-1])
						
			if currentSum > part1 or j == len(numbers): 
				break

			# update current sum	
			currentSum = currentSum + numbers[j] 
			j += 1

	return None, None, None


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)
	
	numbers = []
	for line in lines:
		numbers.append(int(line))

	part1 = computePart1(numbers, 25)
	print("Part1: " + str(part1))	
	print("Part2: " + str(computePart2(numbers, part1)[2]))	