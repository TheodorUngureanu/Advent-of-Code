from __future__ import print_function
# day 19
import Intcode

EXTEND = 1000
MAX_PART1 = 50
MAX_PART2 = 2000

class TractorBeam:
	def __init__(self):
		self.part1 = 0
		self.inputs = []

	def compute_input(self, numbers, x, y):
		numbers_copy = numbers[:]
		self.inputs = [x, y]
		return numbers_copy


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()

	#split into numbers
	numbers = lines[0].split(',')

	#convert to int
	numbers = [int(i) for i in numbers]

	#extend list
	numbers.extend([0] * EXTEND)

	#compute result part 1
	tractor_beam = TractorBeam()
	for i in range(MAX_PART1):
		for j in range(MAX_PART1):
			numbers_copy = tractor_beam.compute_input(numbers, i, j)
			if Intcode.compute_result(numbers_copy, tractor_beam) == 1:
				tractor_beam.part1 += 1
	print("\nPart1:  " + str(tractor_beam.part1))

	#compute result part 2
	y = 99
	x = 0
	# loop until you can make a square 100x100 full of 1
	while True:
		numbers_copy = tractor_beam.compute_input(numbers, x, y)
		#Step1: find a line with 100 "pulled by something" responses
		while Intcode.compute_result(numbers_copy, tractor_beam) == 0:
			x += 1
			numbers_copy = tractor_beam.compute_input(numbers, x, y)
		#Step2: check if you cand make a square. check if above corner contain 1
		x2 = x + 99
		y2 = y -99
		numbers_copy = tractor_beam.compute_input(numbers, x2, y2)
		if Intcode.compute_result(numbers_copy, tractor_beam) == 1:
		  print("Part2:  " + str(x*10000+y2) + "\n")
		  break
		# Step3: update y and find a new line
		y += 1
