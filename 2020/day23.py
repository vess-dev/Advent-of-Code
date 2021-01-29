day_num = 23

import copy

file_load = open("input/day23.txt", "r")
file_prep = file_load.read()
file_load.close()

file_prep = list(map(int, file_prep))
file_start = file_prep[0]
file_in = {}
for temp_cup in file_prep:
	file_in[temp_cup] = file_prep[(file_prep.index(temp_cup) + 1) % 9]

def run():

	def crab(input_in, input_start, input_loop=100):
		input_in = copy.deepcopy(input_in)
		crab_len = len(input_in)
		crab_curr = input_start
		if input_loop != 100:
			input_in[list(input_in.keys())[-1]] = 10
			for temp_num in range(crab_len + 1, 1000001):
				input_in[temp_num] = temp_num + 1
			input_in[1000000] = input_start
			crab_len = 1000000
		for temp_loop in range(0, input_loop):
			crab_pick = []
			crab_pick.append(input_in[crab_curr])
			crab_pick.append(input_in[crab_pick[0]])
			crab_pick.append(input_in[crab_pick[1]])
			crab_target = crab_curr - 1
			while (crab_target in crab_pick) or (crab_target <= 0):
				if crab_target == 0:
					crab_target = crab_len
				else:
					crab_target -= 1
			input_in[crab_curr] = input_in[crab_pick[2]]
			crab_prev = input_in[crab_target]
			input_in[crab_target] = crab_pick[0]
			input_in[crab_pick[2]] = crab_prev
			crab_curr = input_in[crab_curr]
		if input_loop == 100:
			string_total, string_pos = "", 1
			for temp_loop in range(crab_len - 1):
				string_total += str(input_in[string_pos])
				string_pos = input_in[string_pos]
			return string_total
		else:
			return input_in[1] * input_in[input_in[1]]

	return crab(file_in, file_start), crab(file_in, file_start, 10000000)