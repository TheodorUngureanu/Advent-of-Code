# day5
LETTERS = 26

def replace(line):
	aux = None
	while aux != line:
		aux = line
		for i in range(0, LETTERS):
			line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
			line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")
	return line


if __name__ == "__main__":
	with open("day5.in", 'r') as input:
		line = input.read().splitlines()[0]

	# Part1
	new_line = replace(line)
	print("Part1: ", len(new_line))

	# Part 2
	best = len(new_line)
	for i in range(0, LETTERS):
		aux = line
		aux = aux.replace(chr(ord("a") + i),"")
		aux = aux.replace(chr(ord("A") + i),"")
		new_line = replace(aux)
		if len(new_line) < best:
			best = len(new_line)
	print("Part2: " + str(best))
