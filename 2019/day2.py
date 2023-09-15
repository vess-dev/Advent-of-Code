import intcode

day_num = 2

file_load = open("input/day2.txt", "r")
file_prep = file_load.read()
file_load.close()

file_prep = list(map(int, file_prep.split(",")))
file_in = {}
for temp_itr, temp_int in enumerate(file_prep):
	file_in[temp_itr] = temp_int

def run():

	def process(input_in):
		tape_mem = input_in.copy()
		tape_mem[1] = 12
		tape_mem[2] = 2
		comp_main = intcode.Comp()
		comp_main.load(tape_mem)
		comp_main.run()
		return comp_main.mem_tape[0]

	def find(input_in):
		for temp_noun in range(100):
			for temp_verb in range(100):
				tape_mem = input_in.copy()
				tape_mem[1] = temp_noun
				tape_mem[2] = temp_verb
				comp_main = intcode.Comp()
				comp_main.load(tape_mem)
				comp_main.run()
				if comp_main.mem_tape[0] == 19690720:
					return (100 * temp_noun) + temp_verb

	return process(file_in), find(file_in)

if __name__ == "__main__":
	print(run())