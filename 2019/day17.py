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

	MAP_CHECK = [(0, -1), (1, 0), (0, 1), (-1, 0)]

	def render(input_in):
		for temp_int in input_in:
			print(chr(temp_int), end="")
		return
	
	def intake(input_in):
		space_map = {}
		pos_x = 0
		pos_y = 0
		for temp_int in input_in:
			if temp_int == 46:
				pos_x += 1
			elif temp_int == 35:
				space_map[(pos_x, pos_y)] = "#"
				pos_x += 1
			elif temp_int == 10:
				pos_x = 0
				pos_y += 1
			else:
				space_map[(pos_x, pos_y)] = chr(temp_int)
				pos_x += 1
		return space_map
	
	def sect(input_in):
		sect_list = []
		for temp_key in input_in.keys():
			if all((temp_key[0] + temp_new[0], temp_key[1] + temp_new[1]) in input_in for temp_new in MAP_CHECK):
				sect_list.append(temp_key[0] * temp_key[1])
		return sum(sect_list)

	def study(input_in):
		tape_mem = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		comp_main.run()
		space_map = intake(comp_main.mem_output)
		space_sect = sect(space_map)
		return space_sect
	
	def conv(input_in):
		return [ord(temp_char) for temp_char in list(input_in + "\n")] 
	
	def simulate(input_in, *args):
		for temp_func in args:
			func_conv = conv(temp_func)
			input_in.run(func_conv)
		return
	
	def dust(input_in):
		tape_mem = input_in.copy()
		tape_mem[0] = 2
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		comp_main.run()

		func_main = "A"
		func_a = "L1"
		func_b = "2"
		func_c = "3"
		func_video = "y"

		simulate(comp_main, func_main, func_a, func_b, func_c, func_video)

		return

	return study(file_in), dust(file_in)

if __name__ == "__main__":
	print(run())