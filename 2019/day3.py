day_num = 3

file_load = open("input/day3.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = [[[temp_sub[0], int(temp_sub[1:])] for temp_sub in temp_split.split(",")] for temp_split in file_in.split("\n")]

def run():

	def close(input_in):
		wire_points = [[],[]]
		for temp_one, temp_wire in enumerate(input_in):
			wire_xpos = 0
			wire_ypos = 0
			for temp_dir in temp_wire:
				wire_rep = temp_dir[1]
				if temp_dir[0] == "U":
					while wire_rep != 0:
						wire_ypos += 1
						wire_points[temp_one].append((wire_xpos, wire_ypos))
						wire_rep -= 1
				elif temp_dir[0] == "D":
					while wire_rep != 0:
						wire_ypos -= 1
						wire_points[temp_one].append((wire_xpos, wire_ypos))
						wire_rep -= 1
				elif temp_dir[0] == "R":
					while wire_rep != 0:
						wire_xpos += 1
						wire_points[temp_one].append((wire_xpos, wire_ypos))
						wire_rep -= 1
				elif temp_dir[0] == "L":
					while wire_rep != 0:
						wire_xpos -= 1
						wire_points[temp_one].append((wire_xpos, wire_ypos))
						wire_rep -= 1
		wire_crossed = set(wire_points[0]) & set(wire_points[1])
		wire_closest = min([abs(temp_x) + abs(temp_y) for temp_x, temp_y in wire_crossed])
		return wire_closest

	def steps(input_in):
		wire_points = [[], []]
		wire_steps = [[], []]
		for temp_one, temp_wire in enumerate(input_in):
			wire_xpos = 0
			wire_ypos = 0
			wire_step = 0
			for temp_dir in temp_wire:
				wire_rep = temp_dir[1]
				if temp_dir[0] == "U":
					while wire_rep != 0:
						wire_ypos += 1
						wire_points[temp_one].append((wire_xpos, wire_ypos))
						wire_rep -= 1
						wire_step += 1
						wire_steps[temp_one].append(wire_step)
				elif temp_dir[0] == "D":
					while wire_rep != 0:
						wire_ypos -= 1
						wire_points[temp_one].append((wire_xpos, wire_ypos))
						wire_rep -= 1
						wire_step += 1
						wire_steps[temp_one].append(wire_step)
				elif temp_dir[0] == "R":
					while wire_rep != 0:
						wire_xpos += 1
						wire_points[temp_one].append((wire_xpos, wire_ypos))
						wire_rep -= 1
						wire_step += 1
						wire_steps[temp_one].append(wire_step)
				elif temp_dir[0] == "L":
					while wire_rep != 0:
						wire_xpos -= 1
						wire_points[temp_one].append((wire_xpos, wire_ypos))
						wire_rep -= 1
						wire_step += 1
						wire_steps[temp_one].append(wire_step)
		wire_crossed = set(wire_points[0]) & set(wire_points[1])
		wire_sums = []
		for wire_inter in wire_crossed:
			wire_sums.append(wire_steps[0][wire_points[0].index(wire_inter)] + wire_steps[1][wire_points[1].index(wire_inter)])
		return min(wire_sums)

	return close(file_in), steps(file_in)