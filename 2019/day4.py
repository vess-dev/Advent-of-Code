day_num = 4

file_load = open("input/day4.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split("-")))

def run():

	def match(input_in):
		for temp_pass in range(input_in[0], input_in[1] + 1):
			
		return input_in

	return match(file_in)

print(run())