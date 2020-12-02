#day 4
from collections import defaultdict
def parseTime(line):
	 words = line.split()
	 time = words[1][:-1]
	 minute = time.split(':')
	 return int(minute[1])

def argmax(d):
	best = None
	for k,v in d.items():
		if best is None or v > d[best]:
			best = k
	return best

if __name__ == "__main__":
	with open("day4.in", 'r') as input:
		lines = input.read().splitlines()

	lines.sort()

	#Part1
	GUARDS = defaultdict(int)
	GUARDS_MINUTES = defaultdict(lambda: defaultdict(int))
	guard = None
	start_sleep = None
	for line in lines:
		current_time = parseTime(line)
		if 'begins shift' in line:
			guard = int(line.split()[3][1:])
			start_sleep = None
		elif 'falls asleep' in line:
			start_sleep = current_time
		elif 'wakes up' in line:
			for i in range(start_sleep, current_time):
				GUARDS_MINUTES[guard][i] += 1
				GUARDS[guard] += 1


	#searching max time asleep and guard
	best_guard = None
	for key, value in GUARDS.items():
		if best_guard is None or value > GUARDS[best_guard]:
			best_guard = key

	print("Guard:" + str(best_guard))

	best_min = None
	for key, value in GUARDS_MINUTES[best_guard].items():
		if best_min is None or value > GUARDS_MINUTES[best_guard][best_min]:
			best_min = key
	print("Best minute:" + str(best_min))
	print("Part 1: " + str(best_guard * best_min))


	#Part2
	GUARDS = defaultdict(int)
	GUARDS_MINUTES = defaultdict(int)
	guard = None
	start_sleep = None
	for line in lines:
		current_time = parseTime(line)
		if 'begins shift' in line:
			guard = int(line.split()[3][1:])
			start_sleep = None
		elif 'falls asleep' in line:
			start_sleep = current_time
		elif 'wakes up' in line:
			for i in range(start_sleep, current_time):
				GUARDS_MINUTES[(guard, i)] += 1
				GUARDS[guard] += 1


	#searching max time asleep and guard
	best_guard = None
	for key, value in GUARDS_MINUTES.items():
		if best_guard is None or value > GUARDS_MINUTES[best_guard]:
			best_guard = key

	print("Part 2: " + str(best_guard[0] * best_guard[1]))
