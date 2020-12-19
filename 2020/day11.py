day_num = 11

import copy

file_load = open("input/day11.txt", "r")
file_prep = file_load.read()
file_load.close()
file_prep = file_prep.split("\n")
file_prep = [list(temp_line) for temp_line in file_prep]

file_in = [len(file_prep), {}]

for temp_ypos, temp_line in enumerate(file_prep):
	for temp_xpos, temp_spot in enumerate(temp_line):
		if temp_spot == "L":
			file_in[1][(temp_xpos, temp_ypos)] = "L"

def run():

	def update(input_in, input_near):
		input_new = copy.deepcopy(input_in)
		seat_angles = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		for temp_seat in input_in[1]:
			seat_close = 0
			for temp_angle in seat_angles:
				if input_near == 4:
					seat_check = (temp_seat[0] + temp_angle[0], temp_seat[1] + temp_angle[1])
					if seat_check in input_in[1]:
						if input_in[1][seat_check] == "#":
							seat_close += 1
				elif input_near == 5:
					seat_reach = [temp_seat[0], temp_seat[1]]
					while (0 <= seat_reach[0] < input_in[0]) and (0 <= seat_reach[1] < input_in[0]):
						seat_reach = [seat_reach[0] + temp_angle[0], seat_reach[1] + temp_angle[1]]
						seat_check = (seat_reach[0], seat_reach[1])
						if seat_check in input_in[1]:
							if input_in[1][seat_check] == "#":
								seat_close += 1
							break
			if seat_close == 0:
				if input_in[1][temp_seat] == "L":
					input_new[1][temp_seat] = "#"
			elif seat_close >= input_near:
				if input_in[1][temp_seat] == "#":
					input_new[1][temp_seat] = "L"
		return input_new

	def stable(input_in, input_near):
		input_new = input_in
		while True:
			input_old = input_new
			input_new = update(input_new, input_near)
			if input_old[1] == input_new[1]:
				seat_total = 0
				for temp_seat in input_new[1]:
					if input_new[1][temp_seat] == "#":
						seat_total += 1
				return seat_total

	return stable(file_in, 4), stable(file_in, 5)