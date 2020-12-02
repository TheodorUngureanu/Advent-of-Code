#day 4
from collections import Counter
# defining input
MIN = 156218
MAX = 652527

# function for checkin part 1 rules
def check_rules(number):
	# making a string list with all digits from number
	string_list = list(str(number))
	# checking the rules for part 1
	# increasing order and 2 same digits
	if len(set(string_list)) == len(string_list) or string_list != sorted(string_list):
		return False
	return True


# function for checking part 2 rules
def check_more_occurance(number):
	# making a string list with all digits from number
	number = list(str(number))
	# dictionary containing each digits occurance number
	occurance_dictionary = Counter(number)

	for key in occurance_dictionary:
		if occurance_dictionary[key] == 2:		# if we find a sequence of digits it means that we respect the rule
			return True
	return False


if __name__ == "__main__":
	# Part1
	number_list = []	      # list of numbers respecting the part 1 rules
	for number in range(MIN, MAX + 1):
		if check_rules(number):
			number_list.append(number)
	print("\nPart 1:  " + str(len(number_list)))


	# Part 2
	number_list_part2 = []	  # list of numbers respecting the part 1 rules
	for number in number_list:
		if check_more_occurance(number):
			number_list_part2.append(number)
	print("Part 2:  " + str(len(number_list_part2)) + "\n")
