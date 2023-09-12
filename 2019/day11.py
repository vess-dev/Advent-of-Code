import intcode

day_num = 11

file_load = open("input/day11.txt", "r")
file_prep = file_load.read()
file_load.close()

file_prep = list(map(int, file_prep.split(",")))
file_in = {}
for temp_itr, temp_int in enumerate(file_prep):
	file_in[temp_itr] = temp_int

def run():

	def paint(input_in):
		mem_tape = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(mem_tape)
		comp_main.run([0], input_wait=True)
		print(comp_main.mem_out)
		return

	return paint(file_in)

if __name__ == "__main__":
	print(run())