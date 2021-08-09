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

	def edges(input_in, input_full=False):
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
		if input_full:
			tile_edges.append(input_in[0][::-1])
			tile_edges.append(tile_right[::-1])
			tile_edges.append(input_in[-1][::-1])
			tile_edges.append(tile_left[::-1])
		return tile_edges

	def cut(input_in):
		tile_cut = []
		for temp_line in input_in[1:len(input_in)-1]:
			tile_cut.append(temp_line[1:len(temp_line)-1])
		return tile_cut

	def prepare(input_in, input_level):
		tile_prep = {}
		for temp_tile in input_in:
			if input_level:
				tile_new = {"halfedge":edges(temp_tile[1], False), "alledge":edges(temp_tile[1], True), "orig":temp_tile[1], "cut":cut(temp_tile[1]), "pos":[0, 0], "con":0}
			else:
				tile_new = {"alledge":edges(temp_tile[1], True), "con":0}
			tile_prep[temp_tile[0]] = tile_new
		for temp_lhs in tile_prep:
			tile_con = 0
			for temp_rhs in tile_prep:
				if temp_lhs != temp_rhs:
					if any(temp_lhsline in tile_prep[temp_rhs]["alledge"] for temp_lhsline in tile_prep[temp_lhs]["alledge"]):
						tile_prep[temp_lhs]["con"] += 1
		return tile_prep

	def corner(input_in):
		tile_prep = prepare(input_in, False)
		tile_final = 1
		for temp_tile in tile_prep:
			if tile_prep[temp_tile]["con"] == 2:
				tile_final *= temp_tile
		return tile_final

	def tilerot(input_in):
		tile_rot = [""] * len(input_in["orig"])
		for temp_line in input_in["orig"][::-1]:
			itr_pos = 0
			for temp_char in temp_line:
				tile_rot[itr_pos] += temp_char
				itr_pos += 1
		tile_new = {"halfedge":edges(tile_rot, False), "alledge":edges(tile_rot, True), "orig":tile_rot, "cut":cut(tile_rot), "pos":input_in["pos"], "con":input_in["con"]}
		return tile_new

	def tileflip(input_in):
		tile_flip = []
		for temp_line in input_in["orig"]:
			tile_flip.append(temp_line[::-1])
		tile_new = {"halfedge":edges(tile_flip, False), "alledge":edges(tile_flip, True), "orig":tile_flip, "cut":cut(tile_flip), "pos":input_in["pos"], "con":input_in["con"]}
		return tile_new

	def get(input_in, input_side):
		if input_side == "top":
			return input_in["halfedge"][0]
		elif input_side == "right":
			return input_in["halfedge"][1]
		elif input_side == "bottom":
			return input_in["halfedge"][2]
		elif input_side == "left":
			return input_in["halfedge"][3]

	def tileitr(input_in):
		itr_curr = 1
		while True:
			yield input_in
			if itr_curr % 5 == 0:
				input_in = tileflip(input_in)
			else:
				input_in = tilerot(input_in)
			itr_curr += 1

	def solve(input_in):
		tile_prep = prepare(input_in, True)
		map_start = False
		map_yet = []
		map_orient = []
		for temp_tile in tile_prep:
			if tile_prep[temp_tile]["con"] == 2 and not map_start:
				map_start = temp_tile
			else:
				map_yet.append(temp_tile)
				map_orient.extend(tile_prep[temp_tile]["alledge"])
		gen_start = tileitr(tile_prep[map_start])
		while (get(tile_prep[map_start], "right") not in map_orient) or (get(tile_prep[map_start], "bottom") not in map_orient):
			tile_prep[map_start] = next(gen_start)
		map_width = int(math.sqrt(len(input_in)))
		map_y = 0
		map_next = map_start
		map_anchor = map_start
		while map_y != map_width:
			map_x = 1
			while map_x != map_width:
				check_right = get(tile_prep[map_next], "right")
				check_bottom = None
				for temp_tile in map_yet:
					if check_right in tile_prep[temp_tile]["alledge"]:
						gen_tile = tileitr(tile_prep[temp_tile])
						while check_right != get(tile_prep[temp_tile], "left"):
							tile_prep[temp_tile] = next(gen_tile)
						map_next = temp_tile
						tile_prep[temp_tile]["pos"] = [map_x, map_y]
						map_yet.remove(temp_tile)
						break
				map_x += 1
			map_x = 0
			map_y += 1
			check_bottom = get(tile_prep[map_anchor], "bottom")
			for temp_tile in map_yet:
				if check_bottom in tile_prep[temp_tile]["alledge"]:
					gen_tile = tileitr(tile_prep[temp_tile])
					while check_bottom != get(tile_prep[temp_tile], "top"):
						tile_prep[temp_tile] = next(gen_tile)
					map_next = temp_tile
					map_anchor = temp_tile
					tile_prep[temp_tile]["pos"] = [map_x, map_y]
					map_yet.remove(temp_tile)
					break
		return tile_prep

	def stitch(input_in):
		tile_prep = solve(input_in)
		map_width = int(math.sqrt(len(input_in)))
		map_scale = len(input_in[0][1][0]) - 2
		map_x = 0
		map_y = 0
		map_omega = [""] * (map_width * map_scale)
		while map_y != map_width:
			while map_x != map_width:
				for temp_tile in tile_prep:
					if tile_prep[temp_tile]["pos"] == [map_x, map_y]:
						tile_offset = 0
						for temp_line in tile_prep[temp_tile]["cut"]:
							map_omega[tile_offset + (map_y * map_scale)] += temp_line
							tile_offset += 1
						break
				map_x += 1
			map_x = 0
			map_y += 1
		return map_omega

	def window(input_in):
		itr_pos = 0
		while True:
			if itr_pos + 47 <= len(input_in):
				yield input_in[itr_pos:itr_pos+47]
			else:
				yield None
			itr_pos += 1

	def cmp(input_in):
		for temp_pair in input_in:
			if temp_pair[0] != "#":
				continue
			elif (temp_pair[0] == "#") and (temp_pair[0] == temp_pair[1]):
				continue
			else:
				return False
		return True

	def ness(input_in):
		map_scan = "".join(input_in)
		gen_scan = window(map_scan)
		map_target = "#.....#....##....##....###.....#..#..#..#..#..#"
		map_found = 0
		for temp_window in gen_scan:
			if temp_window:
				comp_zip = zip(map_target, temp_window)
				if cmp(comp_zip):
					map_found += 1
			else:
				break
		return map_found

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
			if itr_curr % 5 == 0:
				input_in = mapflip(input_in)
			else:
				input_in = maprot(input_in)
			itr_curr += 1

	def rough(input_in):
		map_omega = stitch(input_in)
		gen_map = mapitr(map_omega)
		map_found = ness(next(gen_map))
		while map_found == 0:
			print("Nope, next...")
			map_found = ness(next(gen_map))
		return "".join(map_omega).count("#") - (15 * map_found)

	return corner(file_in), rough(file_in)

print(run())