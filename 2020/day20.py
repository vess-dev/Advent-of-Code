day_num = 20

import math

file_load = open("input/day20.txt", "r")
file_prep = file_load.read()
file_load.close()

file_prep = file_prep.split("\n\n")

file_in = []

for temp_tile in file_prep:
	tile_struct = [0, []]
	tile_split = temp_tile.split("\n")
	tile_struct[0] = int(tile_split[0].split(" ")[1].replace(":", ""))
	tile_struct[1].extend(tile_split[1:])
	file_in.append(tile_struct)

def run():

	def edges(input_in):
		tile_edges = []
		# Top, right, bottom, left, flips.
		tile_edges.append(input_in[0])
		tile_left, tile_right = "", ""
		for temp_line in input_in:
			tile_left += temp_line[0]
			tile_right += temp_line[-1]
		tile_edges.append(tile_right)
		tile_edges.append(input_in[-1])
		tile_edges.append(tile_left)
		tile_edges.append(input_in[0][::-1])
		tile_edges.append(tile_right[::-1])
		tile_edges.append(input_in[-1][::-1])
		tile_edges.append(tile_left[::-1])
		return tile_edges

	def solve(input_in):
		tile_edges = {}
		for temp_tile in input_in:
			# (Con)nectIDs, (Edge)s, (Orig)inal.
			tile_edges[temp_tile[0]] = {"con":[], "edges":edges(temp_tile[1]), "tile":temp_tile[1], "cut":[], "offset":[0, 0]}
		for temp_tile in tile_edges:
			for temp_comp in tile_edges:
				if temp_tile != temp_comp:
					if any(temp_edge in tile_edges[temp_comp]["edges"] for temp_edge in tile_edges[temp_tile]["edges"]):
						tile_edges[temp_tile]["con"].append(temp_comp)
		return tile_edges

	def corner(input_in):
		tile_edges = solve(input_in)
		tile_total = 1
		for temp_tile in tile_edges:
			if len(tile_edges[temp_tile]["con"]) == 2:
				tile_total *= temp_tile
		return tile_total

	def cut(input_in):
		tile_cut = []
		for temp_line in input_in[1:-1]:
			tile_cut.append(temp_line[1:-1])
		return tile_cut

	def get(input_in, input_side):
		tile_left, tile_right = "", ""
		for temp_line in input_in["tile"]:
			tile_left += temp_line[0]
			tile_right += temp_line[-1]
		if input_side == "up":
			side_ret = input_in["tile"][0]
		elif input_side == "down":
			side_ret = input_in["tile"][-1]
		elif input_side == "left":
			side_ret = tile_left
		elif input_side == "right":
			side_ret = tile_right
		return side_ret

	def flip(input_in):
		tile_flip = []
		input_in = copy.deepcopy(input_in)
		for temp_line in input_in["tile"]:
			tile_flip.append(temp_line[::-1])
		input_in["tile"] = tile_flip
		input_in["edges"] = edges(input_in["tile"])
		return input_in

	def rot(input_in):
		input_in = copy.deepcopy(input_in)
		tile_rot = ["" for temp_itr in range(len(input_in["tile"]))]
		for temp_line in input_in["tile"]:
			for temp_itr, temp_char in enumerate(temp_line):
				tile_rot[temp_itr] = temp_char + tile_rot[temp_itr]
		input_in["tile"] = tile_rot
		input_in["edges"] = edges(input_in["tile"])
		return input_in

	def touchy(input_in, input_tile):
		tile_touchy = []
		for temp_tile in input_in[input_tile]["con"]:
			tile_touchy.extend(input_in[temp_tile]["edges"])
		return tile_touchy

	def align(input_in, input_match):
		
		return

	def ness(input_in):
		tile_edges = solve(input_in)
		map_done = []
		for temp_tile in tile_edges:
			if len(tile_edges[temp_tile]["con"]) == 2:
				map_start = temp_tile
				map_done.append(temp_tile)
				break
		while get(tile_edges[map_start], "right") not in touchy(tile_edges, map_start):
			tile_edges[map_start] = rot(tile_edges[map_start])
		while get(tile_edges[map_start], "down") not in touchy(tile_edges, map_start):
			tile_edges[map_start] = rot(tile_edges[map_start])
		return

	return corner(file_in), ness(file_in)

print(run())