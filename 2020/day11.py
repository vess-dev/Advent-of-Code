day_num = 11

import copy

file_load = open("input/day11.txt", "r")
file_prep = file_load.read()
file_load.close()
file_prep = file_prep.split("\n")

file_in = [len(file_prep), []]
for temp_line in file_prep:
	file_in[1].append(list(temp_line))

def run():

	def update(input_in, input_near):
		input_new = copy.deepcopy(input_in)
		seat_angles = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		for temp_x in range(0, input_in[0]):
			for temp_y in range(0, input_in[0]):
				if input_in[1][temp_x][temp_y] != ".":
					seat_close = 0
					for temp_angle in seat_angles:
						if input_near == 4:
							if (0 <= (temp_x + temp_angle[0]) <= input_in[0] - 1) and (0 <= (temp_y + temp_angle[1]) <= input_in[0] - 1):
								if input_in[1][temp_x + temp_angle[0]][temp_y + temp_angle[1]] == "#":
									seat_close += 1
						elif input_near == 5:
							pos_x, pos_y = temp_x, temp_y
							while True:
								pos_x += temp_angle[0]
								pos_y += temp_angle[1]
								if (0 <= pos_x <= input_in[0] - 1) and (0 <= pos_y <= input_in[0] - 1):
									if input_in[1][pos_x][pos_y] == "#":
										seat_close += 1
										break
									elif input_in[1][pos_x][pos_y] == "L":
										break
								else:
									break
					if seat_close == 0:
						if input_new[1][temp_x][temp_y] == "L":
							input_new[1][temp_x][temp_y] = "#"
					elif seat_close >= input_near:
						if input_new[1][temp_x][temp_y] == "#":
							input_new[1][temp_x][temp_y] = "L"
		return input_new

	def stable(input_in, input_near):
		input_new = copy.deepcopy(input_in)
		while True:
			input_old = input_new
			input_new = update(input_new, input_near)
			seat_total = 0
			if input_old[1] == input_new[1]:
				for temp_line in input_new[1]:
					seat_total += temp_line.count("#")
				return seat_total

	return stable(file_in, 4), stable(file_in, 5)