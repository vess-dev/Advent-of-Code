day_num = 22

import copy

file_load = open("input/day22.txt", "r")
file_in = file_load.read()
file_load.close()

file_in = file_in.replace("Player 1:\n","")
file_in = file_in.replace("Player 2:\n","")
file_in = file_in.split("\n\n")
file_in[0] = list(map(int, file_in[0].split("\n")))
file_in[1] = list(map(int, file_in[1].split("\n")))

def run():

	def rec(input_in, input_top, input_rec):
		input_in = copy.deepcopy(input_in)
		if input_rec:
			round_his = []
		while all(len(temp_deck) > 0 for temp_deck in input_in):
			if input_rec and not input_top:
				if (input_in[0] in round_his) or (input_in[1] in round_his):
					return "one"
				round_his.append(copy.deepcopy(input_in[0]))
				round_his.append(copy.deepcopy(input_in[1]))
			player_one, player_two = input_in[0].pop(0), input_in[1].pop(0)
			if (len(input_in[0]) >= player_one) and (len(input_in[1]) >= player_two) and input_rec:
				if rec([input_in[0][:player_one], input_in[1][:player_two]], False, True) == "one":
					input_in[0].append(player_one)
					input_in[0].append(player_two)
				else:
					input_in[1].append(player_two)
					input_in[1].append(player_one)
			else:
				if player_one > player_two:
					input_in[0].append(player_one)
					input_in[0].append(player_two)
				elif player_one < player_two:
					input_in[1].append(player_two)
					input_in[1].append(player_one)
		if input_top:
			for temp_deck in input_in:
				if len(temp_deck) != 0:
					total_score = 0
					for temp_itr, temp_num in enumerate(reversed(temp_deck), 1):
						total_score += temp_itr * temp_num
					return total_score
		elif len(input_in[0]) != 0:
			return "one"
		elif len(input_in[1]) != 0:
			return "two"

	return rec(file_in, True, False), rec(file_in, True, True)