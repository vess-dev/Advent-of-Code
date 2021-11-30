import math

day_num = 10

file_load = open("input/day10.txt", "r")
file_prep = file_load.read()
file_load.close()

file_in = []
file_prep = file_prep.split("\n")
for temp_x, temp_row in enumerate(file_prep):
	for temp_y, temp_char in enumerate(temp_row):
		if temp_char == "#":
			file_in.append((temp_x, temp_y))

def run():

	def delta(input_in, input_targ):
		return  (input_targ[0] - input_in[0], input_targ[1] - input_in[1])

	def station(input_in):
		astr_count = {}
		for temp_astr in input_in:
			astr_count[temp_astr] = 0
		for temp_base in input_in:
			astr_sight = set()
			for temp_targ in input_in:
				if temp_base != temp_targ:
					astr_delta = delta(temp_base, temp_targ)
					astr_gcd = math.gcd(astr_delta[0], astr_delta[1])
					if astr_gcd > 1:
						flag_see = True
						for temp_step in range(1, astr_gcd):
							astr_check = (int(temp_base[0] + (astr_delta[0] / astr_gcd * temp_step)) , int(temp_base[1] + (astr_delta[1] / astr_gcd * temp_step)))
							if astr_check in input_in:
								flag_see = False
								break
						if flag_see:
							astr_sight.add(temp_targ)
					else:
						astr_sight.add(temp_targ)
					astr_count[temp_base] = len(astr_sight)
		print(astr_count)
		astr_max = 0
		astr_final = (0, 0)
		for temp_astr in astr_count:
			if astr_count[temp_astr] > astr_max:
				astr_max = astr_count[temp_astr]
				astr_final = temp_astr
		return astr_final

	return station(file_in)

if __name__ == "__main__":
	print(run())