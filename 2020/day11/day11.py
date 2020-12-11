#day 11  - run with python3
import copy 


def checkIndex(pos, sizeLines, sizeColumns):
	if 0 <= pos[0] < sizeLines and 0 <= pos[1] < sizeColumns:
		return True
	return False


# if all valid neighbours seats are occupied return true
def getNeighoursOcupationPart1(seatsMap, seatPosition, linesNr, columnsNr):
	line = seatPosition[0]
	column = seatPosition[1]
	up = line - 1
	down = line + 1
	left = column - 1
	right = column + 1

	# all 8 neighbours
	neighbours = [(line, left), (up, left), (up, column), (up, right),
				  (line, right), (down, right), (down, column), (down, left)]
	
	valid_neighbours = []
	for neighPos in neighbours:
		if checkIndex(neighPos, linesNr, columnsNr) and seatsMap[neighPos[0]][neighPos[1]] != '.':
			valid_neighbours.append(neighPos)
	
	# check if valid neighbours seats are all occupied
	occupiedSeats = 0
	for neighPos in valid_neighbours:
		if seatsMap[neighPos[0]][neighPos[1]] == '#':
			occupiedSeats += 1
	return occupiedSeats


def computePart1(seatsMap):
	local_map = seatsMap
	linesNr = len(seatsMap)
	columnsNr = len(seatsMap[0])

	new_map = [[ '.' for i in range(columnsNr) ] for j in range(linesNr)]

	while True:
		for i in range(linesNr):
			for j in range(columnsNr):
				if local_map[i][j] == 'L' and getNeighoursOcupationPart1(local_map, (i,j), linesNr, columnsNr) == 0:
					# occupy seat
					new_map[i][j] = '#'

				elif local_map[i][j] == '#' and getNeighoursOcupationPart1(local_map, (i,j), linesNr, columnsNr) >= 4:
					# free the seat
					new_map[i][j] = 'L'

		if new_map == local_map:
			break
		else:
			local_map =  copy.deepcopy(new_map)

	occupiedSeats = 0
	for row in local_map:
		occupiedSeats += row.count('#')

	return occupiedSeats



# if all valid neighbours seats are occupied return true
def getNeighoursOcupationPart2(seatsMap, seatPosition, linesNr, columnsNr):
	line = seatPosition[0]
	column = seatPosition[1]
	up = -1
	down = 1
	left = -1
	right = 1

	# all 8 neighbours
	directions = [(0, left), (up, left), (up, 0), (up, right),
				  (0, right), (down, right), (down, 0), (down, left)]
	
	occupiedSeats = 0
	for direction in directions:
		pos_X = line + direction[0]
		pos_Y = column + direction[1]

		while checkIndex((pos_X, pos_Y), linesNr, columnsNr):
			if seatsMap[pos_X][pos_Y] == '#':
				occupiedSeats += 1
				break

			elif seatsMap[pos_X][pos_Y] == 'L':
				break
			
			pos_X += direction[0]
			pos_Y += direction[1]
	
	return occupiedSeats


def computePart2(seatsMaps):
	local_map = seatsMap
	linesNr = len(seatsMap)
	columnsNr = len(seatsMap[0])

	new_map = [[ '.' for i in range(columnsNr) ] for j in range(linesNr)]

	while True:
		for i in range(linesNr):
			for j in range(columnsNr):
				if local_map[i][j] == 'L' and getNeighoursOcupationPart2(local_map, (i,j), linesNr, columnsNr) == 0:
					# occupy seat
					new_map[i][j] = '#'

				elif local_map[i][j] == '#' and getNeighoursOcupationPart2(local_map, (i,j), linesNr, columnsNr) >= 5:
					# free the seat
					new_map[i][j] = 'L'

		if new_map == local_map:
			break
		else:
			local_map =  copy.deepcopy(new_map)

	occupiedSeats = 0
	for row in local_map:
		occupiedSeats += row.count('#')

	return occupiedSeats


def printMap(seatsMap):
	for row in seatsMap:
		for column in row:
			print(column, end ="") 
		print("\n", end ="")


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)
	
	seatsMap = []
	for i in range(len(lines)):
		seatsMap.append(list(lines[i]))

	# printMap(seatsMap)

	print("Part1: " + str(computePart1(seatsMap)))	
	print("Part2: " + str(computePart2(seatsMap)))	
