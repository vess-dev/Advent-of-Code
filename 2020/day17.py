day_num = 17

import copy

file_load = open("input/day17.txt", "r")
file_prep = file_load.read()
file_load.close()

file_in = set()

file_prep = [list(temp_itr) for temp_itr in file_prep.split("\n")]
for temp_ypos, temp_y in enumerate(file_prep):
	for temp_xpos, temp_x in enumerate(temp_y):
		if temp_x == "#":
			file_in.add((temp_xpos, temp_ypos, 0, 0))

def run():

	def neigh(input_in, input_four, cord_tup):
		close_arr = []
		close_total = 0
		if input_four:
			input_w = 2
		else:
			input_w = 0
		for temp_x in range(-1,2):
			for temp_y in range(-1,2):
				for temp_z in range(-1,2):
					for temp_w in range(-1, input_w):
						if input_four:
							cord_test = (temp_x + cord_tup[0], temp_y + cord_tup[1], temp_z + cord_tup[2], temp_w + cord_tup[3])
						else:
							cord_test = (temp_x + cord_tup[0], temp_y + cord_tup[1], temp_z + cord_tup[2], 0)
						if cord_test != cord_tup:
							if cord_test not in input_in:
								close_arr.append(cord_test)
							if cord_test in input_in:
								close_total += 1
		return close_arr, close_total

	def cycle(input_in, input_four):
		input_new = set()
		input_checked = set()
		for temp_check in input_in:
			for temp_neigh in neigh(input_in, input_four, temp_check)[0]:
				if temp_neigh not in input_checked:
					if neigh(input_in, input_four, temp_neigh)[1] == 3:
						input_new.add(temp_neigh)
					input_checked.add(temp_neigh)
			if neigh(input_in, input_four, temp_check)[1] in [2, 3]:
				input_new.add(temp_check) 
		return input_new

	def six(input_in):
		input_one = copy.deepcopy(input_in)
		input_two = copy.deepcopy(input_in)
		for temp_rep in range(6):
			input_one = cycle(input_one, False)
			input_two = cycle(input_two, True)
		return len(input_one), len(input_two)

	return six(file_in)