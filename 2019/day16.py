day_num = 16

file_load = open("input/day16.txt", "r")
file_prep = file_load.read()
file_load.close()

file_in = list(map(int, list(str(file_prep))))

def run():

	PATTERN_BASE = [0, 1, 0, -1]

	def index(input_in, input_pos, input_len):
		return ((input_pos + 1) // (input_in + 1)) % input_len

	def fft(input_in):
		list_new = input_in.copy()
		len_all = len(input_in)
		len_2 = len(input_in) // 2
		len_3 = len(input_in) // 3
		for temp_index in range(len_3):
			num_sum = 0
			for temp_pos in range(len_all):
				pattern_index = index(temp_index, temp_pos, len(PATTERN_BASE))
				num_sum += input_in[temp_pos] * PATTERN_BASE[pattern_index]
			list_new[temp_index] = abs(num_sum) % 10
		for temp_index in range(len_3, len_2):
			num_sum = 0
			for temp_pos in range(len(input_in)):
				pattern_index = index(temp_index, temp_pos, len(PATTERN_BASE))
				if pattern_index == 1:
					num_sum += input_in[temp_pos]
			list_new[temp_index] = abs(num_sum) % 10
		sum_partial = sum(input_in[len_2:])
		sum_current = 0
		for temp_index in range(len_2, len_all):
			list_new[temp_index] = (sum_partial - sum_current) % 10
			sum_current += input_in[temp_index]
		return list_new
	
	def subset(input_in, input_max):
		return int("".join(map(str, input_in[0:input_max])))

	def loop(input_in, input_rep):
		loop_list = input_in.copy()
		for temp_loop in range(input_rep):
			loop_list = fft(loop_list)
		return subset(loop_list, 8)
	
	def giga(input_in, temp_rep):
		giga_offset = subset(input_in, 7)
		giga_list = (input_in.copy() * 10_000)[giga_offset:]
		for temp_loop in range(temp_rep):
			sum_partial = sum(giga_list)
			sum_current = 0
			for temp_index in range(len(giga_list)):
				sum_old = sum_current
				sum_current += giga_list[temp_index]
				giga_list[temp_index] = (sum_partial - sum_old) % 10
		return subset(giga_list, 8)

	return loop(file_in, 100), giga(file_in, 100)

if __name__ == "__main__":
	print(run())