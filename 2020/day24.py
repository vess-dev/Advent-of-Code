day_num = 24

import copy

file_load = open("input/day24.txt", "r")
file_prep = file_load.read()
file_load.close()

file_in = []
token_list = ["ne", "se", "e", "nw", "sw", "w"]

file_prep = file_prep.split("\n")
for temp_tile in file_prep:
	tile_path = []
	while temp_tile != "":
		for temp_token in token_list:
			if temp_tile.startswith(temp_token):
				tile_path.append(temp_token)
				temp_tile = temp_tile[len(temp_token):]
	file_in.append(tile_path)

def run():

	def dir(input_in, input_pos):
		if input_in == "ne": return (input_pos[0] + 1, input_pos[1] - 1)
		elif input_in == "se": return (input_pos[0], input_pos[1] + 1)
		elif input_in == "e": return (input_pos[0] + 1, input_pos[1])
		elif input_in == "nw": return (input_pos[0], input_pos[1] - 1)
		elif input_in == "sw": return (input_pos[0] - 1, input_pos[1] + 1)
		elif input_in == "w": return (input_pos[0] - 1, input_pos[1])

	def touch(input_in, input_pos):
		tile_neigh = 0
		dir_list = ["ne", "se", "e", "nw", "sw", "w"]
		for temp_dir in dir_list:
			tile_check = dir(temp_dir, input_pos)
			if tile_check in input_in:
				if not input_in[tile_check]:
					tile_neigh += 1
		return tile_neigh

	def flip(input_in, input_part):
		floor_grid = {}
		dir_list = ["ne", "se", "e", "nw", "sw", "w"]
		for temp_tile in input_in:
			pos_start = (0, 0)
			for temp_dir in temp_tile:
				pos_start = dir(temp_dir, pos_start)
			if pos_start in floor_grid:
				floor_grid[pos_start] = not floor_grid[pos_start]
			else:
				floor_grid[pos_start] = False
		if input_part:
			for temp_day in range(100):
				floor_old = copy.deepcopy(floor_grid)
				for temp_tile in list(floor_old.keys()):
					if not floor_old[temp_tile]:
						tile_neigh = touch(floor_old, temp_tile)
						if (tile_neigh == 0) or (tile_neigh > 2):
							floor_grid[temp_tile] = True
					for temp_dir in dir_list:
						if temp_dir not in floor_old:
							tile_check = dir(temp_dir, temp_tile)
							tile_neigh = touch(floor_old, tile_check)
							if tile_neigh == 2:
								floor_grid[tile_check] = False
		return list(floor_grid.values()).count(False)

	return flip(file_in, False), flip(file_in, True)