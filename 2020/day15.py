day_num = 15

file_load = open("input/day15.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split(",")))

def run():

	def game(input_in, round_hunt):
		num_last = {}
		for temp_pos, temp_num in enumerate(input_in, 1):
			num_last[temp_num] = temp_pos
		game_round = len(input_in)
		game_next = 0
		for game_round in range(len(input_in) + 1, round_hunt):
			if game_next in num_last:
				temp_next = game_round - num_last[game_next]
				num_last[game_next] = game_round
				game_next = temp_next
			else:
				num_last[game_next] = game_round
				game_next = 0
		return game_next

	return game(file_in, 2020), game(file_in, 30000000)