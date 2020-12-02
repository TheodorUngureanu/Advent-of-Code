# day 14
import math

QUANTITY = 0
NAME = 1

class Recipe:
	def __init__(self, name, quantity, ingredients):
		self.name = name
		self.quantity = quantity
		self.ingredients = ingredients # list of tuples with quantity, material name


def print_cookbook(big_list):
	for material in big_list:
		print('to make', big_list[material].quantity, ' of ', material, 'we need: ',big_list[material].ingredients)

# compute a list with order of computing
def compute_stages(big_list):
	# base element. no recipe for it.
	stages = {"ORE": 0}
	while len(stages) < len(big_list):
		for material in big_list:
			# if material is already instages continue
			if material in stages:
				continue
			# look if his ingredients are in stages
			statement = False
			for ingredient in big_list[material].ingredients:
				if ingredient[NAME] not in stages:
					statement = True
			# if not all of his ingredients are discovered continue
			if statement == True:
				continue
			# if this is a new material and all his ingredient are already discovered
			# -> update his stage
			tmp_stages = []
			for ingredient in big_list[material].ingredients:
				tmp_stages.append(stages[ingredient[NAME]])
			stages[material] = max(tmp_stages) + 1
	return stages


def compute_part1(big_list, stages, number):
	need_element = {"FUEL":number}
	while len(need_element) > 1 or "ORE" not in need_element:
		# get material with the higher stage
		material = max(need_element, key=lambda x: stages[x])
		# quantity required of material
		quantity = need_element[material]
		del need_element[material]
		res_quantity = big_list[material].quantity	  # what quantity we can do one time
		ingredients = big_list[material].ingredients  # list of necessar ingredients
		for ingredient in ingredients:
			if ingredient[NAME] not in need_element:  # if element not in need element list
				need_element[ingredient[NAME]] = 0
			# update element(material) quantity number required
			need_element[ingredient[NAME]] += math.ceil(quantity/res_quantity) * ingredient[QUANTITY]
	return need_element["ORE"]


def compute_part2(big_list, stages, ore):
	# ore for computing 1 fuel unit
	ore_for_one_fuel = compute_part1(big_list, stages, 1)
	possible_remain_fuel = ore / ore_for_one_fuel
	#loop
	while True:
		# bureteforce. try to find max fuel quantity
		used_ore = compute_part1(big_list, stages, possible_remain_fuel)
		possible_remain_fuel += (ore - used_ore) / ore_for_one_fuel
		if used_ore > ore:
			break
	return possible_remain_fuel


if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()

	# dictionary containing every ingredient and how to produce it
	big_list = {}
	#split every line
	for line in lines:
		input_string, output = line.split(" => ")
		output = output.split(' ')
		inputs = input_string.split(", ")
		tmp = []
		for material in inputs:
			material = material.split(' ')
			tmp.append((int(material[0]), material[1]))		# tuple with quantity, material name
		big_list[output[1]] = Recipe(output[1], int(output[0]), tmp[:])

	# uncomment for printing cookbook
	# print_cookbook(big_list)
	stages = compute_stages(big_list)
	# print("STAGE OF CREATION:")
	# for elem in stages:
	# 	print(elem, stages[elem])

	# compute part 1
	part1 = compute_part1(big_list, stages, 1)
	print("\nPart1:  " + str(int(part1)))

	# compute part 2
	part2 = compute_part2(big_list, stages, 1000000000000)
	print("Part2:  " + str(int(part2)) + "\n")
