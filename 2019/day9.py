import intcode

day_num = 9

file_load = open("input/day9.txt", "r")
file_prep = file_load.read()
file_load.close()

file_prep = list(map(int, file_prep.split(",")))
file_in = {}
for temp_itr, temp_int in enumerate(file_prep):
	file_in[temp_itr] = temp_int

def run():

	def boost(input_in):
		tape_mem = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		comp_main.run([1])
		return comp_main.last()

	def coord(input_in):
		tape_mem = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		comp_main.run([2])
		return comp_main.last()


	return boost(file_in), coord(file_in)

if __name__ == "__main__":
	print(run())