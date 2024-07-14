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
	MAP_CARD = ["N", "E", "S", "W"]
	MAP_DIR = dict(zip(MAP_CARD, MAP_CHECK))
	MAP_START = {
		"^": "N",
		">": "E",
		"v": "S",
		"<": "W",
	}
	MAP_VALID = {
		"N": {"W", "E"},
		"E": {"N", "S"},
		"S": {"W", "E"},
		"W": {"N", "S"},
	}
	MAP_TURN = {
		("N", "E"): "R",
		("N", "W"): "L",
		("E", "S"): "R",
		("E", "N"): "L",
		("S", "W"): "R",
		("S", "E"): "L",
		("W", "N"): "R",
		("W", "S"): "L",
	}
	MAP_TURNS = ["L", "R"]
	MAIN_LEN = 20
	SUB_LEN = 3

	def render(input_in):
		for temp_int in input_in:
			print(chr(temp_int), end="")
		return
	
	def intake(input_in):
		space_map = {}
		pos_x = 0
		pos_y = 0
		pos_start = (0, 0)
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
				pos_start = (pos_x, pos_y)
				pos_x += 1
		return space_map, pos_start
	
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
		space_map, _ = intake(comp_main.mem_output)
		space_sect = sect(space_map)
		return space_sect
	
	def conv(input_in):
		return [ord(temp_char) for temp_char in list(input_in + "\n")] 
	
	def simulate(input_in, *args):
		for temp_func in args:
			func_conv = conv(temp_func)
			input_in.run(func_conv)
		return
	
	def step(input_in, input_mod):
		return (input_in[0]+input_mod[0], input_in[1]+input_mod[1])
	
	def walk(input_in, input_start):
		path_pos = input_start
		path_dir = MAP_START[input_in[input_start]]
		path_full = []
		path_count = 0
		while True:
			path_check = step(path_pos, MAP_DIR[path_dir])
			if path_check in input_in:
				path_pos = path_check
			else:
				path_old = path_dir
				for temp_check in [(step(path_pos, MAP_DIR[temp_dir]), temp_dir) for temp_dir in MAP_VALID[path_dir]]:
					if temp_check[0] in input_in:
						path_pos = temp_check[0]
						if path_count:
							path_full.append(str(path_count))
							path_count = 0
						path_full.append(MAP_TURN[(path_dir, temp_check[1])])
						path_dir = temp_check[1]
				if path_old == path_dir:
					path_full.append(str(path_count))
					break
			path_count += 1
		return path_full
	
	def subcount(input_in, input_sub):
		list_count = 0
		list_len = len(input_sub)
		for temp_itr in range(len(input_in) - list_len + 1):
			if input_in[temp_itr:temp_itr + list_len] == input_sub:
				list_count += 1
		return list_count
	
	def subdel(input_in, input_sub):
		itr_pos = 0
		out_list = []
		while itr_pos < len(input_in):
			if input_in[itr_pos:itr_pos+len(input_sub)] == input_sub:
				itr_pos += len(input_sub)
			else:
				out_list.append(input_in[itr_pos])
				itr_pos += 1
		return out_list
	
	def window(input_in, input_len):
		itr_pos = 0
		while True:
			if itr_pos + input_len <= len(input_in):
				yield input_in[itr_pos:itr_pos+input_len]
			else:
				yield None
			itr_pos += 1
	
	def slide(input_in, input_max):
		slide_size = input_max
		while slide_size >= SUB_LEN:
			gen_window = window(input_in, slide_size)
			while gen_next := next(gen_window):
				if gen_next[0] in MAP_TURNS:
					if gen_next[-1] not in MAP_TURNS:
						if subcount(input_in, gen_next) > 1:
							return subdel(input_in, gen_next), gen_next
			slide_size -= 1
	
	def dust(input_in):
		tape_mem = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		comp_main.run()
		render(comp_main.mem_output)
		space_map, pos_start = intake(comp_main.mem_output)
		print(space_map)
		print(pos_start)
		print()
		space_path = walk(space_map, pos_start)
		print(space_path)
		print()
		slide_test = "R,8,R,8,R,4,R,4,R,8,L,6,L,2,R,4,R,4,R,8,R,8,R,8,L,6,L,2".split(",")
		slide_max = (MAIN_LEN - (SUB_LEN * 3) - SUB_LEN)
		slide_list = []
		while slide_test:
			print(slide_test, end="")
			slide_test, slide_next = slide(slide_test, slide_max)
			slide_max -= len(slide_next)
			print(" : ", slide_next)
			slide_list.append(slide_next)
		print(slide_list)
		return

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