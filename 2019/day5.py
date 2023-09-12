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
		tape_mem = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		tape_input = [1]
		while not comp_main.flag_halt:
			comp_main.run(input_debug=True)
			if comp_main.flag_input:
				comp_main.flag_payload = tape_input.pop(0)
		return comp_main.mem_output[0]

	def test(input_in):
		tape_mem = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		return comp_main.run([5])

	return diag(file_in)

if __name__ == "__main__":
	print(run())