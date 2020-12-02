#day 2

def getInterval(string):
	interval = string.split(' ')[0]
	return (int(interval.split('-')[0]), int(interval.split('-')[1]))


def getLetter(string):
	return string.split(' ')[1]


def checkPart1(word, interval, letter):
	counter = word.count(letter)
	if counter >= interval[0] and counter <= interval[1]:
		return 1
	else:
		return 0


def checkPart2(word, interval, letter):
	if ((word[interval[0]-1] == letter and word[interval[1]-1] != letter) or
		(word[interval[0]-1] != letter and word[interval[1]-1] == letter)):
		return 1
	return 0

if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)

	part1 = part2 = 0

	for line in lines:
		aux = line.split(': ')
		word = aux[1]
		interval = getInterval(aux[0])
		letter = getLetter(aux[0])

		# solve part1
		part1 += checkPart1(word, interval, letter)

		# solve part2
		part2 += checkPart2(word, interval, letter)

	print("Part1: " + str(part1))
	print("Part1: " + str(part2))
