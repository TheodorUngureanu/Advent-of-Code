from __future__ import print_function
# day 15
import Intcode

EXTEND = 1000
MAX = 40

class Droid:
	objects = {"WALL":0, "clear":1, "target":2}
	directions = {1:[0,1], 2:[0,-1], 3:[-1,0], 4:[1,0]}
	undo_moves = {1:2, 2:1, 3:4, 4:3}
	x = 0
	y = 0

	def __init__(self, numbers):
		self.matrix = [['.' for j in range(MAX)] for i in range(MAX)]
		self.map = {}
		self.numbers = numbers
		self.inputs = []
		self.outputs = []

	def discover(self, x, y):
		for direction in range(1,5):
			dx, dy = self.directions[direction]
			new_x = x + dx
			new_y = y + dy

			# if position is already discovered continue
			if (new_x, new_y) in self.map:
				continue

			self.inputs.append(direction)
			self.numbers, out = Intcode.compute_result(self.numbers, self)
			self.map[(new_x, new_y)] = out

			# if we discover a wall we should undo the move
			if out == 1:
				self.discover(new_x, new_y)
				self.inputs.append(self.undo_moves[direction])
				self.numbers, out = Intcode.compute_result(self.numbers, self)
			elif out == 1:
				self.inputs.append(self.undo_moves[direction])
				self.numbers, out = Intcode.compute_result(self.numbers, self)

	def get_offset(self):
		offset_x = 0
		offset_y = 0
		for elem in self.map:
			if elem[0] < offset_x:
				offset_x = elem[0]
			if elem[1] < offset_y:
				offset_y = elem[1]
		return abs(offset_x), abs(offset_y)


	def print_map(self):
		# prepare for nice display
		offset_x, offset_y = self.get_offset()
		for elem in self.map:
			if self.map[elem] == 0:
				self.matrix[elem[0] + offset_x][elem[1] + offset_y] = "X"
			elif self.map[elem] == 1:
				self.matrix[elem[0] + offset_x][elem[1] + offset_y] = " "
			elif self.map[elem] == 2:
				self.matrix[elem[0] + offset_x][elem[1] + offset_y] = "O"

		# display nice on the screen
		for i in range(MAX):
			for j in range(MAX):
				if(i==offset_x and j==offset_y):
					print("S", end = '')
				else:
					print(self.matrix[i][j], end = '')
			print()


	def BFS(self,x_start_pos, y_start_pos):
		#TODO
		queue = [(x_start_pos, y_start_pos, 0)]
		visited = set()
		min_to_target = (1000000000000, 0, 0)
		maxSteps = 0

		while queue != []:
			x, y, steps = queue.pop(0)
			maxSteps = max(maxSteps, steps)
			# in case we arrive at the target
			if self.map[(x,y)] == 2:
				min_to_target = min(min_to_target, (steps, x, y))
			# mark position as visited
			visited.add((x,y))
			for direction in range(1,5):
				dx, dy = self.directions[direction]
				new_x = x + dx
				new_y = y + dy
				# if it is visited or ????
				if ((new_x, new_y) in visited or (new_x, new_y) not in self.map or
					 self.map[(new_x, new_y)] == self.objects["WALL"]):
					 continue
				else:
					queue.append((new_x, new_y, steps+1))
		print(min_to_target, maxSteps)
		return min_to_target, maxSteps


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
	droid = Droid(numbers)
	droid.discover(0,0)
	droid.print_map()
	droid.BFS(0,0)

	# compute part 1
	part1, x, y = droid.BFS(0,0)[0]
	print("\nPart1:  " + str(part1))

	# compute part 2
	print(x, y)
	part2 = droid.BFS(x,y)[1]
	print("Part2:  " + str(part2) + "\n")
