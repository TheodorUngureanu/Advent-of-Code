# day 12
import copy

STEPS = 1000

class Moon:
	def __init__(self, x, y, z, vx, vy, vz):
		self.x = x
		self.y = y
		self.z = z
		self.vx = vx
		self.vy = vy
		self.vz = vz

	def __str__(self):
		return ("pos= <x=: " + str(self.x) + ", y= " + str(self.y) +
				", z= " + str(self.z) +
				">, vel= <x= " + str(self.vx) + ", y= " + str(self.vy) +
				", z= " + str(self.vz) + ">")

# given the input line return x,y,z values for position and velocity
def compute_coordinates(line):
	x = y = z = vx = vy = vz = 0
	x = int(line[0][1])
	y = int(line[1][1])
	z = int(line[2][1])
	vx = 0
	vy = 0
	vz = 0
	return x, y, z, vx, vy, vz

# function for applying gravity
def apply_gravity(moon1, moon2):
	# for x
	if moon1.x > moon2.x:
		moon1.vx -= 1
		moon2.vx += 1
	elif  moon1.x < moon2.x:
		moon1.vx += 1
		moon2.vx -= 1

	# for y
	if moon1.y > moon2.y:
		moon1.vy -= 1
		moon2.vy += 1
	elif  moon1.y < moon2.y:
		moon1.vy += 1
		moon2.vy -= 1

	# for z
	if moon1.z > moon2.z:
		moon1.vz -= 1
		moon2.vz += 1
	elif  moon1.z < moon2.z:
		moon1.vz += 1
		moon2.vz -= 1

# function for applying velocity
def apply_velocity(moon):
	moon.x += moon.vx
	moon.y += moon.vy
	moon.z += moon.vz

# calculate energy for a moon
def compute_energy(moon):
	pot = abs(moon.x) + abs(moon.y) + abs(moon.z)
	kin = abs(moon.vx) + abs(moon.vy) + abs(moon.vz)
	total = pot * kin
	return pot, kin, total


def compute_part1(dict):
	for i in range(STEPS):
		# apply gravity
		for j in  range(4):
			for k in range(j + 1, 4):
				apply_gravity(dict[j], dict[k])

		# apply velocity
		for elem in dict:
			apply_velocity(dict[elem])

		total_energy = 0
		for elem in dict:
			pot, kin, total = compute_energy(dict[elem])
			if i == STEPS - 1:
				total_energy += total
	return total_energy


def compute_part2(dict, orig_coords):
	#start with axis. save coorinates for axis: [[x1..x4],[y1..y4],[z1..z4]]
	coord_list = [[], [], []]
	for i in range(len(dict)):
		coord_list[0].append(orig_coords[i].x)
		coord_list[1].append(orig_coords[i].y)
		coord_list[2].append(orig_coords[i].z)
	# period (STEPS)
	period = 1
	#compute for each axis x, y, z
	for axis in coord_list:
		temp_velocity_value = [0] * len(axis)
		aux = 0
		while aux == 0 or any(temp_velocity_value):	 # while velocity is not 0
			# i for retain moon, x1 is the x,y,x coordinate from one axis
			for i, x1 in enumerate(axis):
				for x2 in axis:
					# compute velocity
					if x1 < x2:
						temp_velocity_value[i] += 1
					elif x1 > x2:
						temp_velocity_value[i] -= 1
			# update new velocity for each moon
			for i in range(4):
				axis[i] += temp_velocity_value[i]
			aux += 1
		# for each axis, after a number of steps we will reach same velocity (0,0,0)
		# to reach same velocity and same axis coordinate we should multiply each
		# axis steps to find final number of steps
		period *= aux
	return period


if __name__ == "__main__":
	# initialization of moons
	dict = {}
	# initialization of total energy for part 1
	total_energy = 0
	# dict for part2
	orig_coords = {}

	with open("input", 'r') as input:
		lines = input.read().splitlines()

		for i in range(len(lines)):
			# eliminate <> simbols
			lines[i] = lines[i][1:-1]
			lines[i] = lines[i].split(', ')
			for j in range(len(lines[i])):
				lines[i][j] = lines[i][j].split('=')
			#create instance of each moon
			x, y, z, vx, vy, vz = compute_coordinates(lines[i])
			dict[i] = Moon(x, y, z, vx, vy, vz)
			# save initial moon coordinates
			orig_coords[i] = Moon(x, y, z, vx, vy, vz)

	# part 1
	dict_part1 = copy.deepcopy(dict)
	total_energy = compute_part1(dict_part1)
	print("\nPart1:\n  " + str(total_energy))

	# part 2
	dict_part2 = copy.deepcopy(dict)
	result = compute_part2(dict, orig_coords)
	print("\nPart2:\n  " + str(result) + "\n")
