day_num = 11

import copy

file_load = open("input/day11.txt", "r")
file_prep = file_load.read()
file_load.close()
file_prep = file_prep.split("\n")

file_in = []
for temp_line in file_prep:
	file_in.append(list(temp_line))

def run():

	def update(input_in):
		input_new = copy.deepcopy(input_in)
		seat_angles = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		input_len = len(input_in)
		for temp_x in range(0, input_len):
			for temp_y in range(0, input_len):
				if input_in[temp_x][temp_y] != ".":
					seat_close = 0
					for temp_angle in seat_angles:
						if 0 <= (temp_x + temp_angle[0]) <= input_len - 1:
							if 0 <= (temp_y + temp_angle[1]) <= input_len - 1:
								if input_in[temp_x + temp_angle[0]][temp_y + temp_angle[1]] == "#":
									seat_close += 1
					if seat_close == 0:
						if input_new[temp_x][temp_y] == "L":
							input_new[temp_x][temp_y] = "#"
					elif seat_close >= 4:
						if input_new[temp_x][temp_y] == "#":
							input_new[temp_x][temp_y] = "L"
		return input_new

	def stable(input_in):
		while True:
			input_old = input_in
			input_in = update(input_in)
			seat_total = 0
			if input_old == input_in:
				for temp_line in input_in:
					seat_total += temp_line.count("#")
				return seat_total

	def angle(input_in):
		input_new = copy.deepcopy(input_in)
		seat_angles = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		input_len = len(input_in)
		for temp_x in range(0, input_len):
			for temp_y in range(0, input_len):
				if input_in[temp_x][temp_y] != ".":
					seat_close = 0
					for temp_angle in seat_angles:
						pos_x, pos_y = temp_x, temp_y
						while True:
							pos_x += temp_angle[0]
							pos_y += temp_angle[1]
							if (0 <= pos_x <= input_len - 1) and (0 <= pos_y <= input_len - 1):
								if input_in[pos_x][pos_y] == "#":
									seat_close += 1
									break
								elif input_in[pos_x][pos_y] == "L": break
							else: break
					if seat_close == 0:
						if input_new[temp_x][temp_y] == "L":
							input_new[temp_x][temp_y] = "#"
					elif seat_close >= 5:
						if input_new[temp_x][temp_y] == "#":
							input_new[temp_x][temp_y] = "L"
		return input_new

	def see(input_in):
		while True:
			input_old = input_in
			input_in = angle(input_in)
			seat_total = 0
			if input_old == input_in:
				for temp_line in input_in:
					seat_total += temp_line.count("#")
				return seat_total

	return stable(file_in), see(file_in)