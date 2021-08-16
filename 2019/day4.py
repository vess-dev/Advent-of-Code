day_num = 4

file_load = open("input/day4.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split("-")))

def run():

	def match(input_in):
		pass_total = 0
		pass_list = []
		for temp_pass in range(input_in[0], input_in[1] + 1):
			pass_step = list(zip(list(str(temp_pass)), list(str(temp_pass))[1:]))
			if all(temp_one <= temp_two for temp_one, temp_two in pass_step):
				if any(temp_one == temp_two for temp_one, temp_two in pass_step):
					pass_total += 1
					pass_list.append(temp_pass)
		return pass_total, strict(pass_list)

	def strict(input_in):
		pass_total = 0
		for temp_pass in input_in:
			pass_str = str(temp_pass)
			if any((pass_str.count(temp_char) == 2) for temp_char in pass_str):
				pass_total += 1
		return pass_total

	return match(file_in)