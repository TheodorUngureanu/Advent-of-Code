#day 5

def computeRow(string, interval):
	for char in string:
		if char in ["F", "L"] :
			interval[1] = int(interval[0] + int((interval[1] - interval[0])/ 2)) 
		else:
			interval[0] = int(interval [1] - int((interval[1] - interval[0]) / 2))

	return interval[0]


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)
	
	seats = [] 

	for line in lines:
		row = computeRow(line[:-3], [0, 127])
		column = computeRow(line[-3:], [0, 7])
		seats.append(row * 8 + column)

	# print(seats)
	print("Part1: " + str(max(seats)))

	# because we can have some seats missing from very front and back
	newSeats = range(min(seats), max(seats))

	# if there is right pair part that differ from the left -> that is our missing place
	for leftSeat, rightSeat in zip(sorted(seats), newSeats):
		if leftSeat != rightSeat:
			print("Part2: " + str(rightSeat))
			break
