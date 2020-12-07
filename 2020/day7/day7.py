#day 7

def computePart1(luggages, containers):
	bags = set()	

	while len(containers) > 0:
		aux = []
		for bag in luggages:
			for p in containers:
				if p in luggages[bag]:
					aux.append(bag)
		
		containers = set(aux)
		bags.update(containers)

	return len(bags)


def computePart2(luggages, bag):
	part2 = 0
	if luggages[bag] == {}:
		return 0

	else:
		for bagColor, number in luggages[bag].items():
			part2 += number + number * computePart2(luggages, bagColor)
		return part2
	

if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)
	
	luggages = {}
	for line in lines:
		aux = line[:-1].replace(" bags","").replace(" bag","").split(" contain ")
		content = aux[1].split(", ")

		tmp = {}
		for bag in content:
			if bag == "no other":
				pass
			else:
				tmp[bag[2:]] = int(bag[0])
		luggages[aux[0]] = tmp

	#DEBUG
	# for luggage in luggages:
	# 	print(luggage, "->", luggages[luggage])
	# print("\n")
	
	print("Part1: " + str(computePart1(luggages, ["shiny gold"])))
	print("Part2: " + str(computePart2(luggages, "shiny gold")))