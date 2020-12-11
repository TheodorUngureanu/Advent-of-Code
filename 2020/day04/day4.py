#day 4

import itertools

ACCEPTED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


# validate if passport field are the one requested
def validateFieldNumbers(dictionary):
	if (len(dictionary.keys()) == len(ACCEPTED_KEYS) or 
			(len(dictionary.keys()) == len(ACCEPTED_KEYS) - 1 and 'cid' not in dictionary)):
			return 1
	return 0


# validate if the passport field content constraints are validated
def validateFieldRule(dictionary):
	for key, value in dictionary.items():
		if key == 'byr':
			if not (value.isdigit() and int(value) >= 1920 and int(value) <= 2002):
				return 0

		elif key == 'iyr':
			if not (value.isdigit() and int(value) >= 2010 and int(value) <= 2020):
				return 0

		elif key == 'eyr':
			if not (value.isdigit() and int(value) >= 2020 and int(value) <= 2030):
				return 0

		elif key == 'hgt':
			if not (value.endswith('cm') or value.endswith('in')):
				return 0
			else:
				if value.endswith('cm') and not (int(value[:-2]) >= 150 and int(value[:-2]) <= 193):
					return 0

				if value.endswith('in') and not (int(value[:-2]) >= 59 and int(value[:-2]) <= 76):
					return 0

		elif key == 'hcl':
			if not (value.startswith('#') and len(value[1:]) == 6):
				return 0

		elif key == 'ecl':
			if value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
				return 0

		elif key == 'pid':
			if not (value.isdigit() and len(value) == 9):
				return 0

		elif key == 'cid':
			pass
	
	return 1	
	

def checkPart1(passports):
	counter = 0
	for key, value in passports.items():
		tmpDict = value
		counter += validateFieldNumbers(tmpDict)

	return counter


def checkPart2(passports):
	counter = 0
	for key, value in passports.items():
		tmpDict = value
		validateFieldRule(tmpDict)

		if validateFieldNumbers(tmpDict) == 1 and validateFieldRule(tmpDict) == 1:
			counter += 1
	return counter
		

if __name__ == "__main__":
	with open("input", 'r') as input:
		lines = input.read().splitlines()
		# print(lines)
	
	passports = {}
	id = 0
	aux = {}
	for i in range (0,len(lines)):
		if lines[i] is "":
			passports[id] = aux
			aux = {}
			id +=1
		else:
			tmpLine = lines[i].split(' ')
			tmpList = []
			tmpList.extend([i.split(':')[0], i.split(':')[1]] for i in tmpLine) 
			merged = list(itertools.chain.from_iterable(tmpList))
			it = iter(merged)
			tmpDict = dict(zip(it, it))
			aux.update(tmpDict)

			# last line condition
			if i == len(lines) - 1:
				passports[id] = aux
				aux = {}
				id +=1


	# print(passports)
	print("Part1: " + str(checkPart1(passports)))
	print("Part2: " + str(checkPart2(passports)))