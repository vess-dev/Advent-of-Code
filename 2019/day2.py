day_num = 2

file_load = open("input/day2.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split(",")))

def run():

	def comp(input_in):
		mem_tape = input_in.copy()
		mem_pos = 0
		while True:
			if mem_tape[mem_pos] == 1:
				mem_tape[mem_tape[mem_pos + 3]] = mem_tape[mem_tape[mem_pos + 1]] + mem_tape[mem_tape[mem_pos + 2]]
			elif mem_tape[mem_pos] == 2:
				mem_tape[mem_tape[mem_pos + 3]] = mem_tape[mem_tape[mem_pos + 1]] * mem_tape[mem_tape[mem_pos + 2]]
			elif mem_tape[mem_pos] == 99:
				break
			mem_pos += 4
		return mem_tape

	def process(input_in):
		mem_tape = input_in.copy()
		mem_tape[1] = 12
		mem_tape[2] = 2
		return comp(mem_tape)[0]

	def find(input_in):
		for temp_noun in range(100):
			for temp_verb in range(100):
				mem_tape = input_in.copy()
				mem_tape[1] = temp_noun
				mem_tape[2] = temp_verb
				if comp(mem_tape)[0] == 19690720:
					return (100 * temp_noun) + temp_verb

	return process(file_in), find(file_in)