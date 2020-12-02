#day 2

if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		#print(lines)

	#part 1
	for i in range(0,len(lines)):
		#print line
		for j in range(i+1, len(lines)):
			if i != j and int(lines[i]) + int(lines[j]) == 2020:
				print("Part1: " + str(lines[i]) + " " + str(lines[j]) + " " + str(int(lines[i]) * int(lines[j])))


	#part 2
	for i in range(0,len(lines)):
		#print line
		for j in range(i+1, len(lines)):
			for k in range(j+1, len(lines)):
				if int(lines[i]) + int(lines[j]) + int(lines[k]) == 2020:
					print("Part2: " + str(int(lines[i]) * int(lines[j]) * int(lines[k])))
