day_num = 14

file_load = open("input/day14.txt", "r")
file_prep = file_load.read()
file_load.close()
file_prep = file_prep.split("\n")

file_in = []

for temp_com in file_prep:
	if temp_com.startswith("mask"):
		temp_split = temp_com.split(" = ")
		file_in.append((temp_split[0], temp_split[1]))
	elif temp_com.startswith("mem"):
		temp_split = temp_com.split(" = ")
		temp_sub = temp_split[0].split("[")
		temp_loc = int(temp_sub[1][:-1])
		file_in.append((temp_sub[0], temp_loc, int(temp_split[1])))

def run():

	def subnet(input_mask, input_num):
		num_masked = str(bin(input_num)[2:])
		num_masked = list(("0" * (36 - len(num_masked))) + num_masked)
		num_pos = 0
		for temp_char in input_mask:
			if temp_char == "1":
				num_masked[num_pos] = "1"
			elif temp_char == "0":
				num_masked[num_pos] = "0"
			num_pos += 1
		num_masked = int("".join(num_masked), 2)
		return num_masked

	def mask(input_in):
		comp_mem = {}
		comp_mask = ""
		for temp_com in input_in:
			if temp_com[0] == "mask":
				comp_mask = temp_com[1]
			elif temp_com[0] == "mem":
				comp_mem[temp_com[1]] = subnet(comp_mask, temp_com[2])
		return sum(list(comp_mem.values()))

	def getall(input_mask, input_loc):
		comp_locs = []
		loc_split = str(bin(input_loc)[2:])
		loc_split = list(("0" * (36 - len(loc_split))) + loc_split)
		num_x = input_mask.count("X")
		num_float = 2**num_x
		loc_pos = 0
		for temp_float in range(num_float):
			input_masked = list(input_mask)
			float_temp = list(str(bin(temp_float)[2:]))
			float_split = (["0"] * (num_x - len(float_temp))) + float_temp
			float_pos = 0
			for temp_pos, temp_char in enumerate(input_masked):
				if temp_char == "X":
					if float_split[float_pos] == "1":
						input_masked[temp_pos] = "1"
					else:
						input_masked[temp_pos] = "-"
					float_pos += 1
			loc_masked = loc_split
			for temp_pos, temp_char in enumerate(input_masked):
				if temp_char == "1":
					loc_masked[temp_pos] = "1"
				elif temp_char == "-":
					loc_masked[temp_pos] = "0"
			comp_locs.append(int("".join(loc_masked), 2))
			num_float -= 1
		return comp_locs

	def decode(input_in):
		comp_mem = {}
		comp_mask = ""
		for temp_com in input_in:
			if temp_com[0] == "mask":
				comp_mask = temp_com[1]
			elif temp_com[0] == "mem":
				comp_locs = getall(comp_mask, temp_com[1])
				for temp_loc in comp_locs:
					comp_mem[temp_loc] = temp_com[2]
		return sum(list(comp_mem.values()))

	return mask(file_in), decode(file_in)