day_num = 20

import copy
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

	def edge(input_in, input_flip):
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
		if input_flip:
			tile_edges.append(input_in[0][::-1])
			tile_edges.append(tile_right[::-1])
			tile_edges.append(input_in[-1][::-1])
			tile_edges.append(tile_left[::-1])
		return tile_edges

	def cut(input_in):
		tile_cut = []
		for temp_line in input_in[1:-1]:
			tile_cut.append(temp_line[1:-1])
		return tile_cut

	def solve(input_in, input_basic):
		tile_edges = {}
		for temp_tile in input_in:
			# (Con)nectIDs, (Edge)s, (Orig)inal.
			if input_basic:
				tile_edges[temp_tile[0]] = {"con":[], "edge":edge(temp_tile[1], input_basic)}
			else:
				tile_edges[temp_tile[0]] = {"con":[], "edge":edge(temp_tile[1], input_basic), "tile":temp_tile[1], "cut":[], "up":0, "down":0, "left":0, "right":0}
		for temp_tile in tile_edges:
			for temp_comp in tile_edges:
				if temp_tile != temp_comp:
					if any(temp_edge in tile_edges[temp_comp]["edge"] for temp_edge in tile_edges[temp_tile]["edge"]):
						tile_edges[temp_tile]["con"].append(temp_comp)
		return tile_edges

	def corner(input_in):
		tile_edges = solve(input_in, True)
		tile_total = 1
		for temp_tile in tile_edges:
			if len(tile_edges[temp_tile]["con"]) == 2:
				tile_total *= temp_tile
		return tile_total

	def flip(input_in):
		tile_flip = []
		input_in = copy.deepcopy(input_in)
		for temp_line in input_in["tile"]:
			tile_flip.append(temp_line[::-1])
		input_in["tile"] = tile_flip
		input_in["edge"] = edge(input_in["tile"], False)
		return input_in

	def rot(input_in):
		input_in = copy.deepcopy(input_in)
		tile_rot = ["" for temp_itr in range(len(input_in["tile"]))]
		for temp_line in input_in["tile"]:
			for temp_itr, temp_char in enumerate(temp_line):
				tile_rot[temp_itr] = temp_char + tile_rot[temp_itr]
		input_in["tile"] = tile_rot
		input_in["edge"] = edge(input_in["tile"], False)
		return input_in

	def fix(input_in, input_new):
		tile_get = list(set(input_in["edge"]).intersection(input_new["edge"]))
		if tile_get:
			tile_pos = input_in["edge"].index(tile_get[0])
			tile_off = input_new["edge"].index(tile_get[0])
		else:
			#tile_new = flip(input_new)
			print(input_in["edge"])
			print(input_new["edge"])
		check_list = [(0, 2), (1, 3), (2, 0), (3, 1)]
		while (tile_pos, tile_off) not in check_list:
			tile_off = (tile_off + 1) % 4
			input_new = rot(input_new)
		return input_new

	def ness(input_in):
		tile_edges = solve(input_in, False)
		for temp_tile in tile_edges:
			for temp_comp in tile_edges[temp_tile]["con"]:
				tile_edges[temp_comp] = fix(tile_edges[temp_tile], tile_edges[temp_comp])
			#quit()
		return

	return corner(file_in), ness(file_in)

print(run())