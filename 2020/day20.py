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

	def edges(input_in, input_full):
		edges_out = []
		edge_left, edge_right = "", ""
		for temp_line in input_in:
			edge_left += temp_line[0]
			edge_right += temp_line[-1]
		# Top, Bottom, Left, Right
		edges_out.extend([input_in[0], input_in[-1], edge_left, edge_right])
		if input_full:
			edges_out.extend([input_in[0][::-1], input_in[-1][::-1], edge_left[::-1], edge_right[::-1]])
		return edges_out

	def prepare(input_in, input_prepfull):
		prep_out = {}
		for temp_tile in input_in:
			if input_prepfull:
				prep_out[temp_tile[0]] = {"edgehalf":edges(temp_tile[1], False), "edgeall":edges(temp_tile[1], True), "data":temp_tile[1], "pos": [0, 0], "con":0}
			else:
				prep_out[temp_tile[0]] = {"edgeall":edges(temp_tile[1], True), "con":0}
		for temp_lhs in prep_out:
			tile_con = 0
			for temp_rhs in prep_out:
				if temp_lhs != temp_rhs:
					if any(temp_lhsline in prep_out[temp_rhs]["edgeall"] for temp_lhsline in prep_out[temp_lhs]["edgeall"]):
						prep_out[temp_lhs]["con"] += 1
		return prep_out

	def corner(input_in):
		prep_in = prepare(input_in, False)
		id_mult = 1
		for temp_tile in prep_in:
			if prep_in[temp_tile]["con"] == 2:
				id_mult *= temp_tile
		return id_mult

	def tilerot(input_in):
		tile_rot = [""] * len(input_in["data"])
		for temp_line in input_in["data"][::-1]:
			itr_pos = 0
			for temp_char in temp_line:
				tile_rot[itr_pos] += temp_char
				itr_pos += 1
		tile_new = {"edgehalf":edges(tile_rot, False), "edgeall":edges(tile_rot, True), "data":tile_rot, "pos":input_in["pos"], "con":input_in["con"]}
		return tile_new

	def tileflip(input_in):
		tile_flip = []
		for temp_line in input_in["data"]:
			tile_flip.append(temp_line[::-1])
		tile_new = {"edgehalf":edges(tile_flip, False), "edgeall":edges(tile_flip, True), "data":tile_flip, "pos":input_in["pos"], "con":input_in["con"]}
		return tile_new

	def tileitr(input_in):
		itr_curr = 1
		while True:
			yield input_in
			if itr_curr % 4 == 0:
				input_in = tileflip(input_in)
			else:
				input_in = tilerot(input_in)
			itr_curr += 1

	def get(input_in, input_side):
		if input_side == "top":
			return input_in["edgehalf"][0]
		elif input_side == "bottom":
			return input_in["edgehalf"][1]
		elif input_side == "left":
			return input_in["edgehalf"][2]
		elif input_side == "right":
			return input_in["edgehalf"][3]

	def getpos(input_in, input_pos):
		for temp_tile in input_in:
			if input_in[temp_tile]["pos"] == input_pos:
				return temp_tile

	def solve(input_in):
		map_start = None
		map_yet, map_orient = [], []
		for temp_tile in input_in:
			if input_in[temp_tile]["con"] == 2 and not map_start:
				map_start = temp_tile
			else:
				map_yet.append(temp_tile)
				map_orient.extend(input_in[temp_tile]["edgeall"])
		gen_start = tileitr(input_in[map_start])
		while (get(input_in[map_start], "right") not in map_orient) or (get(input_in[map_start], "bottom") not in map_orient):
			input_in[map_start] = next(gen_start)
		map_width = int(math.sqrt(len(input_in)))
		map_y = 0
		map_next, map_anchor = map_start, map_start
		while map_y != map_width:
			map_x = 1
			while map_x != map_width:
				check_right = get(input_in[map_next], "right")
				for temp_tile in map_yet:
					if check_right in input_in[temp_tile]["edgeall"]:
						gen_tile = tileitr(input_in[temp_tile])
						while check_right != get(input_in[temp_tile], "left"):
							input_in[temp_tile] = next(gen_tile)
						map_next = temp_tile
						input_in[temp_tile]["pos"] = [map_x, map_y]
						map_yet.remove(temp_tile)
						map_x += 1
						break
			map_x = 0
			map_y += 1
			check_bottom = get(input_in[map_anchor], "bottom")
			for temp_tile in map_yet:
				if check_bottom in input_in[temp_tile]["edgeall"]:
					gen_tile = tileitr(input_in[temp_tile])
					while check_bottom != get(input_in[temp_tile], "top"):
						input_in[temp_tile] = next(gen_tile)
					map_next = temp_tile
					map_anchor = temp_tile
					input_in[temp_tile]["pos"] = [map_x, map_y]
					map_yet.remove(temp_tile)
					break
		return input_in

	def cut(input_in):
		tile_cut = []
		for temp_line in input_in[1:len(input_in)-1]:
			tile_cut.append(temp_line[1:len(input_in)-1])
		return tile_cut

	def maprot(input_in):
		tile_rot = [""] * len(input_in)
		for temp_line in input_in[::-1]:
			itr_pos = 0
			for temp_char in temp_line:
				tile_rot[itr_pos] += temp_char
				itr_pos += 1
		return tile_rot

	def mapflip(input_in):
		tile_flip = []
		for temp_line in input_in:
			tile_flip.append(temp_line[::-1])
		return tile_flip

	def mapitr(input_in):
		itr_curr = 1
		while True:
			yield input_in
			if itr_curr % 4 == 0:
				input_in = mapflip(input_in)
			else:
				input_in = maprot(input_in)
			itr_curr += 1

	def stitch(input_in):
		map_width = int(math.sqrt(len(input_in)))
		map_x = 0
		map_y = 0
		map_full = [""] * (map_width * 8)
		while map_y != map_width:
			while map_x != map_width:
				tile_offset = 0
				tile_get = input_in[getpos(input_in, [map_x, map_y])]["data"]
				for temp_line in cut(tile_get):
					map_full[tile_offset + (map_y * 8)] += temp_line
					tile_offset += 1
				map_x += 1
			map_x = 0
			map_y += 1
		return map_full

	def window(input_in, input_len):
		itr_pos = 0
		while True:
			if itr_pos + input_len <= len(input_in):
				yield input_in[itr_pos:itr_pos+input_len]
			else:
				yield None
			itr_pos += 1

	def cmp(input_in):
		for temp_pair in input_in:
			if temp_pair[0] != "#":
				continue
			elif temp_pair[0] == "#" and temp_pair[0] == temp_pair[1]:
				continue
			else:
				return False
		return True

	def ness(input_in):
		map_tape = "".join(input_in)
		map_diff = len(input_in[0]) - 20
		scan_target = "..................#." + ("." * map_diff) + "#....##....##....###" + ("." * map_diff) + ".#..#..#..#..#..#..."
		gen_window = window(map_tape, len(scan_target))
		map_found = 0
		for temp_window in gen_window:
			if temp_window:
				scan_zip = zip(scan_target, temp_window)
				if cmp(scan_zip):
					map_found += 1
			else:
				break
		return map_found

	def rough(input_in):
		prep_in = prepare(input_in, True)
		prep_in = solve(prep_in)
		map_stitch = stitch(prep_in)
		gen_map = mapitr(map_stitch)
		map_found = 0
		while map_found == 0:
			map_found = ness(next(gen_map))
		return "".join(map_stitch).count("#") - (15 * map_found)

	return corner(file_in), rough(file_in)