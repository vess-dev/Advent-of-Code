import intcode

day_num = 5

file_load = open("input/day5.txt", "r")
file_prep = file_load.read()
file_load.close()

file_prep = list(map(int, file_prep.split(",")))
file_in = {}
for temp_itr, temp_int in enumerate(file_prep):
	file_in[temp_itr] = temp_int

def run():

	def diag(input_in):
		mem_tape = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(mem_tape)
		return comp_main.run([1])

	def test(input_in):
		mem_tape = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(mem_tape)
		return comp_main.run([5])

	return diag(file_in), test(file_in)

if __name__ == "__main__":
	print(run())