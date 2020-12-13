day_num = 12

file_load = open("input/input12.txt", "r")
file_prep = file_load.read()
file_load.close()
file_prep = file_prep.split("\n")

file_in = []
for temp_dir in file_prep:
	file_in.append([temp_dir[0], int(temp_dir[1:])])

def run():

	def drive(input_in):
		boat_dir = 90
		boat_xpos = 0
		boat_ypos = 0
		for temp_dir in input_in:
			if temp_dir[0] == "N": boat_ypos += temp_dir[1]
			elif temp_dir[0] == "E": boat_xpos += temp_dir[1]
			elif temp_dir[0] == "S": boat_ypos -= temp_dir[1]
			elif temp_dir[0] == "W": boat_xpos -= temp_dir[1]
			elif temp_dir[0] == "L":
				boat_dir -= temp_dir[1]
				boat_dir = boat_dir % 360
			elif temp_dir[0] == "R":
				boat_dir += temp_dir[1]
				boat_dir = boat_dir % 360
			elif temp_dir[0] == "F":
				if boat_dir == 0: boat_ypos += temp_dir[1]
				elif boat_dir == 90: boat_xpos += temp_dir[1]
				elif boat_dir == 180: boat_ypos -= temp_dir[1]
				elif boat_dir == 270: boat_xpos -= temp_dir[1]
		return abs(boat_xpos) + abs(boat_ypos)

	def way(input_in):
		way_xpos = 10
		way_ypos = 1
		boat_xpos = 0
		boat_ypos = 0
		for temp_dir in input_in:
			if temp_dir[0] == "N": way_ypos += temp_dir[1]
			elif temp_dir[0] == "E": way_xpos += temp_dir[1]
			elif temp_dir[0] == "S": way_ypos -= temp_dir[1]
			elif temp_dir[0] == "W": way_xpos -= temp_dir[1]
			elif temp_dir[0] == "L":
				temp_rot = temp_dir[1]
				while temp_rot != 0:
					way_xpos, way_ypos = way_ypos * -1, way_xpos
					temp_rot -= 90
			elif temp_dir[0] == "R":
				temp_rot = temp_dir[1]
				while temp_rot != 0:
					way_xpos, way_ypos = way_ypos, way_xpos * -1
					temp_rot -= 90
			elif temp_dir[0] == "F":
				boat_xpos += way_xpos * temp_dir[1]
				boat_ypos += way_ypos * temp_dir[1]
		return abs(boat_xpos) + abs(boat_ypos)

	return drive(file_in), way(file_in)