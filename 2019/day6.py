day_num = 6

file_load = open("input/day6.txt", "r")
file_prep = file_load.read()
file_load.close()

file_in = []
file_prep = file_prep.split("\n")
for temp_conn in file_prep:
	temp_conn = temp_conn.split(")")
	file_in.append(temp_conn)

def run():

	def make(input_in):
		map_orbit = {}
		for temp_conn in input_in:
			if temp_conn[0] in map_orbit.keys():
				map_orbit[temp_conn[0]].append(temp_conn[1])
			else:
				map_orbit[temp_conn[0]] = [temp_conn[1]]
		return map_orbit

	def walk(input_in, input_next, input_step):
		if input_next in input_in.keys():
			total_steps = input_step
			for temp_next in input_in[input_next]:
				total_steps += walk(input_in, temp_next, input_step + 1)
			return total_steps
		else:
			return input_step

	def count(input_in):
		return walk(make(input_in), "COM", 0)

	def path(input_in, input_target):
		map_steps = []
		if input_target not in input_in.keys():
			for temp_planet in input_in:
				if input_target in input_in[temp_planet]:
					map_steps.append(temp_planet)
					map_curr = temp_planet
					break
		else:
			map_curr = input_target
		while map_curr != "COM":
			for temp_planet in input_in:
				if map_curr in input_in[temp_planet]:
					map_steps.append(temp_planet)
					map_curr = temp_planet
					break
		return map_steps

	def between(input_in):
		map_orbit = make(input_in)
		path_you = path(map_orbit, "YOU")
		path_san = path(map_orbit, "SAN")
		path_both = [temp_planet for temp_planet in path_you if temp_planet in path_san]
		return (len(path_you) - len(path_both)) + (len(path_san) - len(path_both))

	return count(file_in), between(file_in)

if __name__ == "__main__":
	print(run())