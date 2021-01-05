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

	def edge(input_in):
		tile_edges = []
		tile_edges.append(input_in[0])
		tile_edges.append(input_in[-1])
		tile_left, tile_right = "", ""
		for temp_tile in input_in:
			tile_left += temp_tile[0]
			tile_right += temp_tile[-1]
		tile_edges.append(tile_left)
		tile_edges.append(tile_right)
		tile_edges.append(input_in[0][::-1])
		tile_edges.append(input_in[-1][::-1])
		tile_edges.append(tile_left[::-1])
		tile_edges.append(tile_right[::-1])
		return tile_edges

	def cut(input_in):
		tile_cut = []
		for temp_line in input_in[1:-1]:
			tile_cut.append(temp_line[1:-1])
		return tile_cut

	def solve(input_in):
		tile_edges = {}
		for temp_tile in input_in:
			# (Con)nectIDs, (Edge)s, (Orig)inal.
			tile_edges[temp_tile[0]] = {"con":[], "edge":edge(temp_tile[1]), "orig":temp_tile[1], "cut":cut(temp_tile[1])}
		for temp_tile in tile_edges:
			for temp_comp in tile_edges:
				if temp_tile != temp_comp:
					if any(temp_edge in tile_edges[temp_comp]["edge"] for temp_edge in tile_edges[temp_tile]["edge"]):
						tile_edges[temp_tile]["con"].append(temp_comp)
		return tile_edges

	def corner(input_in):
		tile_edges = solve(input_in)
		tile_total = 1
		for temp_tile in tile_edges:
			if len(tile_edges[temp_tile]["con"]) == 2:
				tile_total *= temp_tile
		return tile_total

	def arrange(input_in):
		return

	def ness(input_in):
		tile_edges = solve(input_in)
		for temp_tile in tile_edges:
			print(temp_tile, tile_edges[temp_tile], "\n")
		tile_map = arrange(tile_edges)
		print(tile_map)
		return

	return corner(file_in), ness(file_in)

print(run())