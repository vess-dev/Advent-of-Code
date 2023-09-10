import math

day_num = 10

file_load = open("input/day10.txt", "r")
file_prep = file_load.read()
file_load.close()

file_in = []
file_prep = file_prep.split("\n")
for temp_y, temp_row in enumerate(file_prep):
	for temp_x, temp_char in enumerate(temp_row):
		if temp_char == "#":
			file_in.append((temp_x, temp_y))

def run():

	def delta(input_in, input_targ):
		return  (input_targ[0] - input_in[0], input_targ[1] - input_in[1])

	def sight(input_in, input_base):
		astr_sight = set()
		for temp_targ in input_in:
			if temp_targ != input_base:
				astr_delta = delta(input_base, temp_targ)
				astr_gcd = math.gcd(astr_delta[0], astr_delta[1])
				if astr_gcd > 1:
					flag_see = True
					for temp_step in range(1, astr_gcd):
						astr_check = (int(input_base[0] + (astr_delta[0] / astr_gcd * temp_step)), int(input_base[1] + (astr_delta[1] / astr_gcd * temp_step)))
						if astr_check in input_in:
							flag_see = False
							break
					if flag_see:
						astr_sight.add(temp_targ)
				else:
					astr_sight.add(temp_targ)
		return astr_sight

	def station(input_in):
		astr_count = {}
		for temp_astr in input_in:
			astr_count[temp_astr] = 0
		for temp_base in input_in:
			astr_seen = sight(input_in, temp_base)
			astr_count[temp_base] = len(astr_seen)
		astr_max = 0
		astr_final = (0, 0)
		for temp_astr in astr_count:
			if astr_count[temp_astr] > astr_max:
				astr_max = astr_count[temp_astr]
				astr_final = temp_astr
		return astr_final, astr_max

	def angle(input_in, input_targ):
		angle_radians = math.atan2(input_targ[1]-input_in[1], input_targ[0]-input_in[0])
		angle_degrees = math.degrees(angle_radians)
		return angle_degrees

	def lazer(input_in, input_loc):
		astr_current = input_in
		astr_exploded = 0
		while astr_exploded != 200:
			astr_seen = sight(astr_current, input_loc)
			astr_circle = []
			for temp_astr in astr_seen:
				astr_angle = angle(input_loc, temp_astr)
				astr_circle.append([temp_astr, astr_angle])
			astr_circle.sort(key=lambda temp_astr: temp_astr[1])
			astr_up = None
			for temp_astr in astr_circle:
				if temp_astr[1] >= -90:
					astr_up = temp_astr
					break
			astr_index = astr_circle.index(astr_up)
			astr_circle = astr_circle[astr_index:] + astr_circle[:astr_index]
			while len(astr_circle) != 0:
				astr_boom = astr_circle.pop(0)
				astr_exploded += 1
				astr_current.remove(astr_boom[0])
				if astr_exploded == 200:
					return (astr_boom[0][0] * 100) + astr_boom[0][1]

	output_final, output_max = station(file_in)
	return output_max, lazer(file_in, output_final)

if __name__ == "__main__":
	print(run())