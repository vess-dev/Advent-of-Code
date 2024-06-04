import intcode

day_num = 17

file_load = open("input/day17.txt", "r")
file_prep = file_load.read()
file_load.close()

file_prep = list(map(int, file_prep.split(",")))
file_in = {}
for temp_itr, temp_int in enumerate(file_prep):
	file_in[temp_itr] = temp_int

def run():

	MAP_CHAR = {
		46: ".",
		35: "#",
		94: "&",
		10: "\n",
	}

	MAP_CHECK = [(0, -1), (1, 0), (0, 1), (-1, 0)]

	def render(input_in):
		for temp_int in input_in:
			print(MAP_CHAR[temp_int], end="")
		return
	
	def intake(input_in):
		space_map = {}
		pos_x = 0
		pos_y = 0
		for temp_int in input_in:
			print(temp_int)
			if temp_int == 46:
				pos_x += 1
			elif temp_int == 35:
				pos_x += 1
				space_map[(pos_x, pos_y)] = "#"
			elif temp_int == 10:
				pos_x = 0
				pos_y += 1
			elif temp_int == 94:
				pos_x += 1
				space_map[(pos_x, pos_y)] = "&"
		return space_map
	
	def sect(input_in):
		sect_list = []
		for temp_key in input_in.keys():
			if all((temp_key[0] + temp_new[0], temp_key[1] + temp_new[1]) in input_in for temp_new in MAP_CHECK):
				sect_list.append(temp_key[0] * temp_key[1])
		print(sect_list)
		return sum(sect_list)

	def study(input_in):
		tape_mem = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		comp_main.run()
		render(comp_main.mem_output)
		space_map = intake(comp_main.mem_output)
		space_sect = sect(space_map)
		print(space_sect)
		return

	return study(file_in)

if __name__ == "__main__":
	print(run())