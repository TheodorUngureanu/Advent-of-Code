#day3
import numpy
import math

SIZE = 1000

if __name__ == "__main__":
	with open("day3.in", 'r') as input:
		lines = input.read().splitlines()

	matrix = []
	for i in range(SIZE):
		coloane = []
		for j in range(SIZE):
			coloane.append([])
		matrix.append(coloane)

	for line in lines:
		l = line.split(' ')
		ID = int(l[0][1:])
		left   = int(l[2].split(",")[0])
		top    = int(l[2].split(",")[1][:-1])
		width  = int(l[3].split("x")[0])
		height = int(l[3].split("x")[1])

		for i in range(top, top + height):
			for j in range(left, left + width):
				matrix[i][j].append(ID)

	count = 0
	for i in range(SIZE):
		for j in range(SIZE):
			if len(matrix[i][j]) > 1:
				count += 1
	print("Part 1: " + str(count))



	for line in lines:
		l = line.split(' ')
		ID = int(l[0][1:])
		left   = int(l[2].split(",")[0])
		top    = int(l[2].split(",")[1][:-1])
		width  = int(l[3].split("x")[0])
		height = int(l[3].split("x")[1])
		ok = True
		for i in range(top, top + height):
			for j in range(left, left + width):
				if len(matrix[i][j]) != 1:
					ok = False
		if ok == True:
			print("Part 2: " + str(ID))

	#afisare matrice
	# for i in range(SIZE):
	# 	print(matrix[i])
