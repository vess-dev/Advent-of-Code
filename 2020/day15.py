day_num = 15

file_load = open("input/day15.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split(",")))

def run():

	def add(num_last, num_new, game_round):
		if not num_new in num_last:
			num_last[num_new] = [game_round, game_round]
		else:
			num_last[num_new][1] = num_last[num_new][0]
			num_last[num_new][0] = game_round
		return num_last

	def game(input_in, round_hunt):
		num_last = {}
		for temp_pos, temp_num in enumerate(input_in, 1):
			num_last[temp_num] = [temp_pos, temp_pos]
		game_round = len(input_in)
		game_last = input_in[-1]
		while True:
			game_round += 1
			if game_last in num_last:
				num_new = num_last[game_last][0] - num_last[game_last][1]
				num_last = add(num_last, num_new, game_round)
				game_last = num_new
			else:
				num_last = add(num_last, 0, game_round)
				game_last = num_new
			if game_round == round_hunt:
				return game_last

	return game(file_in, 2020), game(file_in, 30000000)