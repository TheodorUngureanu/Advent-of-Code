#day 10
from collections import defaultdict 


def computePart1(jolts):
	jolt1_Difference = jolt3_Difference = 0

	for i in range(len(jolts) - 1):
		if jolts[i+1] == (jolts[i] + 1):
			jolt1_Difference += 1

		if jolts[i+1] == (jolts[i] + 3):
			jolt3_Difference += 1

	return jolt1_Difference * jolt3_Difference, jolt1_Difference, jolt3_Difference


def computePart2(jolts):
	arrangements = defaultdict(int)
	# device can be used only in one way
	deviceJoltage = jolts.pop()
	arrangements[deviceJoltage] = 1

	for adapter in reversed(jolts):
		arrangements[adapter] = arrangements[adapter + 1] + arrangements[adapter + 2] + arrangements[adapter + 3]

	return arrangements[0]


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)

	jolts = [int(line) for line in lines]
	jolts = [0] + jolts + [max(jolts) + 3]
	jolts.sort()

	print("Part1: " + str(computePart1(jolts)[0]))	
	print("Part1: " + str(computePart2(jolts)))	