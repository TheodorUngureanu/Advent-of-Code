# day 7
import string
from numpy import zeros
from collections import Counter

def check(list1, list2):
	for letter in list1:
		if letter not in list2:
			return False
	return True

if __name__ == "__main__":
	with open("day7.in", 'r') as input:
		lines = input.read().splitlines()

	dictionar = {}
	for letter in string.ascii_uppercase:
		dictionar[str(letter)] = []

	for line in lines:
		dictionar[line[36]].append(line[5])

	answear = ""
	done = []
	for i in range(100):
		tmp = []
		for letter in dictionar:
			if letter not in done and check(dictionar[letter], done):
				done.append(letter)
				tmp.append(letter)
				break
		tmp.sort()
		for l in tmp:
			answear += l
	print("Part 1: " + answear)


	done = []
	working_on = [None] * 5
	time_left = zeros(5, dtype=int)

	for i in range(1000000):
		for j in range(5):
			if working_on[j] is not None:
				time_left[j] -= 1
				if time_left[j] == 0:
					done.append(working_on[j])
					working_on[j] = None

		# print("i: " + str(i) + " litere: " + str(list(string.ascii_uppercase)) + " done:" + str(done))
		done.sort()
		if list(string.ascii_uppercase) == done:
			print("Part 2: " + str(i))
			break

		for j in range(5):
			if working_on[j] is not None:
				continue

			for letter in dictionar:
				if letter not in done and letter not in working_on and check(dictionar[letter], done):
					working_on[j] = letter
					time_left[j] = 60 + ord(letter) - ord('A') + 1
					break
