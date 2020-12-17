day_num = 17

import copy

file_load = open("input/day17.txt", "r")
file_in = file_load.read()
file_load.close()

file_len = len(file_in.split("\n")[0]) + 14
file_in = [[list("." * 7) + list(temp_itr) + list("." * 7) for temp_itr in file_in.split("\n")]]

while len(file_in[0]) != file_len:
	file_in[0].insert(0, (["."] * file_len))
	file_in[0].insert(len(file_in[0]), (["."] * file_len))

while len(file_in) <= file_len:
	file_in.insert(0, [["."] * file_len for _ in range(file_len)])
	file_in.insert(len(file_in), [["."] * file_len for _ in range(file_len)])

def run():

	def peek(input_in, cord_z):
		for temp_y in input_in[cord_z]:
			print("".join(temp_y))
		return

	def alive(input_in):
		alive_total = 0
		input_len = len(input_in[0]) - 1
		for temp_z in range(input_len):
			for temp_y in range(input_len):
				for temp_x in range(input_len):
					if input_in[temp_z][temp_y][temp_x] == "#":
						alive_total += 1
		return alive_total

	def close(input_in, cord_x, cord_y, cord_z):
		close_total = 0
		close_arr = [(-1, 1),(0,1),(1,1),(-1,0),(0,0),(1,0),(-1,-1),(0,-1),(1,-1)]
		for temp_z in range(-1,2):
			for temp_mod in close_arr:
				if temp_z == 0 and temp_mod == (0,0):
					pass
				else:
					if input_in[cord_z + temp_z][cord_y + temp_mod[1]][cord_x + temp_mod[0]] == "#":
						close_total += 1
		return close_total

	def cycle(input_in):
		input_next = copy.deepcopy(input_in)
		input_len = len(input_in[0]) - 1
		for temp_x in range(1, input_len):
			for temp_y in range(1, input_len):
				for temp_z in range(1, input_len):
					if input_in[temp_z][temp_y][temp_x] == ".":
						if close(input_in, temp_x, temp_y, temp_z) == 3:
							input_next[temp_z][temp_y][temp_x] = "#"
					elif input_in[temp_z][temp_y][temp_x] == "#":
						close_count = close(input_in, temp_x, temp_y, temp_z)
						if close_count not in [2, 3]:
							input_next[temp_z][temp_y][temp_x] = "."
						else:
							input_next[temp_z][temp_y][temp_x] = "#"
		return input_next

	def six(input_in):
		input_new = copy.deepcopy(input_in)
		for temp_rep in range(6):
			print(temp_rep + 1)
			input_new = cycle(input_new)
		return alive(input_new)

	return six(file_in)

print(run())