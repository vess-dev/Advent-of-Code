day_num = 10

from functools import lru_cache

file_load = open("input/input10.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split("\n")))
file_in.sort()
file_in = [0] + file_in
file_in.append(file_in[-1] + 3)

def run():

	def diff(input_in):
		diff_1, diff_2, diff_3, input_pos = 0, 0, 0, 0
		while input_pos != len(input_in) - 1:
			diff_check = input_in[input_pos + 1] - input_in[input_pos]
			if diff_check == 1: diff_1 += 1
			elif diff_check == 3: diff_3 += 1
			input_pos += 1
		return diff_1 * diff_3
	
	def arrange(input_in):
		@lru_cache(maxsize = None)
		def jolts(input_max):
			if input_max == input_in[-1]:
				return 1
			diff_total = 0
			for temp_test in range(1, 4):
				if (temp_test + input_max) in input_in:
					diff_total += jolts(temp_test + input_max)
			return diff_total
		return jolts(0)

	return diff(file_in), arrange(file_in)