from __future__ import print_function
import Intcode
import copy
# day 11
# 0:black 1:white
# define
EXTEND = 1000
SIZE_LINE = 50
SIZE_COL = 10
movements = {"up":[0, 1],
			 "down":[0, -1],
			 "left":[-1, 0],
			 "right":[1, 0]}
directions = ["up", "right", "down", "left"]


class Robot:
	def __init__(self):
		self.curent_direction = 0
		self.painted = {}
		self.pos = [5,5]		# so that all coordinates be > 0 in the end

	def move(self, direction):
		if direction == 0:  	# move left
			value = (self.curent_direction - 1) % 4
			self.update(directions[value], value)

		elif direction == 1: 		# move right
			value = (self.curent_direction + 1) % 4
			self.update(directions[value], value)

	def update(self, key, value):
		self.pos[0] += movements[key][0]
		self.pos[1] += movements[key][1]
		self.curent_direction = value

	def paint(self, color):
		self.painted[(self.pos[0], self.pos[1])] = color

	def part2(self):
		message = [' '] * SIZE_LINE * SIZE_COL
		for elem in self.painted:
			i, j = elem
			if self.painted[elem] == 1:
				message[i * SIZE_COL + j] = 'X'
			else:
				message[i * SIZE_COL + j] = ' '

		# print out the letters
		for i in range(SIZE_LINE):
			for j in range(SIZE_COL):
				print(message[i * SIZE_COL + j], end = '')
			print('')


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()

	#split into numbers
	numbers = lines[0].split(',')

	#convert to int
	numbers = [int(i) for i in numbers]

	#extend list
	numbers.extend([0] * EXTEND)
	numbers_part2 =numbers[:]

	# part 1
	robo = Robot()
	#compute result
	robo = Intcode.compute_result(numbers, robo, 0)
	print("\n Part 1: " + str(len(robo.painted)))

	# part 2
	robo = Robot()
	#compute result
	robo = Intcode.compute_result(numbers_part2, robo, 1)
	print(" Part 2:  "+ str(len(robo.painted)))
	robo.part2()
