#day 1
if __name__ == "__main__":
	with open("day1.in", 'r') as input:
		lines = input.read().splitlines()

	suma = 0
	for line in lines:
		suma += int(line)
		#print(line)
	print("SUMA: " + str(suma))

	suma = 0;
	freq_list = {0:True}
	ok = True
	while ok:
		for line in lines:
			suma += int(line)
			if suma in freq_list:
				print("TWICE: ", str(suma))
				ok = False
				break;
			else:
				freq_list[suma] = True
