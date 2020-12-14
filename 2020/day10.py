day_num = 10

file_load = open("input/day10.txt", "r")
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
		plug_list = {0:1}
		for temp_plug in sorted(input_in):
			plug_list[temp_plug] = 0
			for temp_step in range(-1, -4, -1):
				if temp_plug + temp_step in plug_list:
					plug_list[temp_plug] += plug_list[temp_plug + temp_step]
		return list(plug_list.values())[-1]

	return diff(file_in), arrange(file_in[1:-2])