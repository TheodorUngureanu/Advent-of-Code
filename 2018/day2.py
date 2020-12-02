#day2
if __name__ == "__main__":
	with open("day2.in", 'r') as input:
		lines = input.read().splitlines()

	pair = [0, 0]
	for line in lines:
		count = {}
		for c in line:
			if c not in count:
				count[c] = 0
			count[c] += 1

		# print(count)
		ok2 = False
		ok3 = False
		for a in count:
			if count[a] == 2:
				ok2 = True
			if count[a] == 3:
				ok3 = True

		if ok2:
			pair[0] += 1
		if ok3:
			pair[1] += 1

	print("Part 1: " + str(pair[0] * pair[1]))

	for l1 in lines:
		for l2 in lines:
			check = 0
			for i in range(len(l1)):
				if l1[i] != l2[i]:
					check += 1
			if check == 1:
				string = []
				for i in range(len(l1)):
					if l1[i] == l2[i]:
						string.append(l1[i])

	print("Part 2: " + "".join(string))
