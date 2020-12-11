#day 6

from collections import Counter


def computePart1(groups):
	yes = 0
	for key, value in groups.items():
		yes += len(value[0])
	return yes


def computePart2(groups):
	yes = 0
	for key, value in groups.items():
		answers = Counter(value[1])

		for answer, number in answers.items():
			if number == value[2]:
				yes +=1
	return yes


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)
	
	groups = {}
	groupID = 0
	personCounter = 0
	aux = []
	
	for i in range (0, len(lines)):
		if lines[i] is "":
			groups[groupID] = (set(aux), aux, personCounter)
			groupID +=1
			aux = []
			personCounter = 0
			
		else:
			aux.extend(list(lines[i]))
			personCounter +=1

			# last line condition
			if i == len(lines) - 1:
				groups[groupID] = (set(aux), aux, personCounter)
				groupID +=1
				aux = []
				personCounter = 0


	# print(groups)
	print("Part1: " + str(computePart1(groups)))
	print("Part2: " + str(computePart2(groups)))
