import intcode

day_num = 2

file_load = open("input/day2.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split(",")))

def run():

	def process(input_in):
		mem_tape = input_in.copy()
		mem_tape[1] = 12
		mem_tape[2] = 2
		obj_comp = intcode.Comp()
		obj_comp.load(mem_tape)
		while not obj_comp.next():
			continue
		return obj_comp.mem_tape[0]

	def find(input_in):
		for temp_noun in range(100):
			for temp_verb in range(100):
				mem_tape = input_in.copy()
				mem_tape[1] = temp_noun
				mem_tape[2] = temp_verb
				obj_comp = intcode.Comp()
				obj_comp.load(mem_tape)
				while not obj_comp.next():
					continue
				if obj_comp.mem_tape[0] == 19690720:
					return (100 * temp_noun) + temp_verb

	return process(file_in), find(file_in)

if __name__ == "__main__":
	print(run())