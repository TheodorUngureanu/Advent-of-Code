#day 3

movements = {1: (1,1), 2: (3,1), 3: (5,1), 4: (7,1), 5: (1,2)}


def makeMove(i, j, tobogganWidth, right, down):
	return i + down, (j + right) % tobogganWidth


def findTrees(lines, right, down):
	tobogganHeight = len(lines)
	tobogganWidth = len(lines[0])

	i=j=0
	treeCounter = 0
	
	while i < tobogganHeight:
		if lines[i][j] == "#":
			treeCounter += 1
		
		i, j = makeMove(i, j, tobogganWidth, right, down)
	
	return treeCounter	


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)
	
	print("Part1: " + str(findTrees(lines, movements[2][0], movements[2][1])))

	part2 = 1
	for key, (moveRight, moveDown) in movements.items():
		part2 *= findTrees(lines, moveRight, moveDown)
	print("Part2: " + str(part2))
