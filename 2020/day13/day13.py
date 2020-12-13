#day 13
import sys

def computePart1(earliers_timestamp, busIDs):
	tmpTime = sys.maxsize
	tmpBusID = None

	for id in busIDs:
		nextTimestampStop = (earliers_timestamp / id + 1) * id
		if nextTimestampStop - earliers_timestamp < tmpTime:
			tmpTime = nextTimestampStop - earliers_timestamp
			tmpBusID = id

	return tmpTime * tmpBusID


def computePart2(busses):
	# the smallest common multiple (cmmmc)
	cmmmc = int(busses[0])
	timeStamp = 0

	for i in range(1, len(busses)):
		if busses[i] != 'x':
			while (timeStamp + i) % int(busses[i]) != 0:
				timeStamp += cmmmc
			cmmmc *= int(busses[i])
	return timeStamp


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)
	
	earliers_timestamp = int(lines[0])
	busIDs = []
	busses = lines[1].split(',')
	for bus in busses:
		if bus != 'x':
			busIDs.append(int(bus))

	print("Part1: " + str(computePart1(earliers_timestamp, busIDs)))
	print("Part2: " + str(computePart2(busses)))