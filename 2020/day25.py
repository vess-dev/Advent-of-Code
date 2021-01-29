day_num = 25

import copy

file_load = open("input/day25.txt", "r")
file_in = file_load.read()
file_load.close()

file_in = file_in.split("\n")
file_in = list(map(int, file_in))

def run():

	def shake(input_in):
		input_in = copy.deepcopy(input_in)
		num_test = 1
		num_sec = 0
		while num_test not in input_in: 
			num_test = (num_test * 7) % 20201227
			num_sec += 1
		input_in.remove(num_test)
		num_test = input_in[0]
		for temp_loop in range(num_sec - 1):
			num_test = (num_test * input_in[0]) % 20201227
		return num_test

	return shake(file_in)