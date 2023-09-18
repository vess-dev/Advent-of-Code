day_num = 14

file_load = open("input/day14.txt", "r")
file_prep = file_load.read()
file_load.close()

file_in = {}
file_prep = file_prep.split("\n")
for temp_line in file_prep:
	mix_pair = temp_line.split(" => ")
	mix_in = mix_pair[0]
	mix_in = mix_in.split(", ")
	mix_in = [(temp_part.split(" ")[1], int(temp_part.split(" ")[0])) for temp_part in mix_in]
	mix_out = mix_pair[1]
	mix_out = mix_out.split(" ")
	mix_out = (mix_out[1], int(mix_out[0]))
	file_in[mix_out] = mix_in

def run():

	def cook(input_in, input_list):
		list_cooked = []
		for temp_part in input_list:
			if temp_part in input_in:
				list_cooked.extend(input_in[temp_part])
			else:
				list_cooked.append(temp_part)
		return list_cooked

	def bake(input_in):
		print(input_in)
		print()
		list_raw = [("FUEL", 1)]
		for temp_step in range(10):
			list_raw = cook(input_in, list_raw)
			print(list_raw)
		
		return

	return bake(file_in)

if __name__ == "__main__":
	print(run())