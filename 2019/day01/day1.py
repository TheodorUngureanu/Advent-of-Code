#day 1

if __name__ == "__main__":


	with open("input", 'r') as input:
		lines = input.read().splitlines()
		#print(lines)

	#part 1
	suma = 0
	for line in lines:
		#print line
		suma += (int(line) / 3 - 2)
	print("Part1: " + str(suma))


	#part 2
	suma = 0
	for line in lines:
		while (int(line) / 3 - 2) >= 0:
			suma += (int(line) / 3 - 2)
			line = int(line) / 3 - 2
	print("Part2: " + str(suma))

