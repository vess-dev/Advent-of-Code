import intcode
import itertools

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
	MIN_LEN = 8

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

	def shake(input_in):
		input_len = len(input_in)
		slide_len = MAIN_LEN + 1
		slide_matches = {}
		for temp_pos in range(0, input_len - MIN_LEN):
			for temp_width in range(MIN_LEN, slide_len):
				slide_check = input_in[temp_pos:temp_pos + temp_width]
				if slide_check in slide_matches:
					continue
				if (slide_check.startswith(",") or not slide_check.endswith(",") or not (slide_check[0] in MAP_TURNS) or (slide_check[-2] in MAP_TURNS)):
					continue
				if input_in.count(slide_check) >= 2:
					slide_matches[slide_check] = True
		return list(slide_matches.keys())

	def find(input_in, input_matches):
		slide_combos = itertools.combinations(input_matches, 3)
		for temp_tuple in slide_combos:
			if input_in.replace(temp_tuple[0], "").replace(temp_tuple[1], "").replace(temp_tuple[2], "") == "":
				return temp_tuple
		return
	
	def simulate(input_main, *input_funcs):
		for temp_func in input_funcs:
			func_conv = conv(temp_func)
			input_main.run(func_conv)
		return

	def dust(input_in):
		tape_mem = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		comp_main.run()
		space_map, pos_start = intake(comp_main.mem_output)
		space_path = ",".join(walk(space_map, pos_start)) + ","
		slide_matches = shake(space_path)
		slide_find = find(space_path, slide_matches)
		func_main = space_path.replace(slide_find[0], "A,").replace(slide_find[1], "B,").replace(slide_find[2], "C,")[:-1]
		func_a = slide_find[0][:-1]
		func_b = slide_find[1][:-1]
		func_c = slide_find[2][:-1]
		func_video = "n"
		tape_mem[0] = 2
		comp_next = intcode.Comp()
		comp_next.load(tape_mem)
		simulate(comp_next, func_main, func_a, func_b, func_c, func_video)
		return comp_next.status()

	return study(file_in), dust(file_in)

if __name__ == "__main__":
	print(run())