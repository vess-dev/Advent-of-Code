import intcode
import itertools

day_num = 7

file_load = open("input/day7.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split(",")))

def run():

	def ampl(input_in):
		mem_tape = input_in.copy()
		phase_list = list(itertools.permutations([0, 1, 2, 3, 4]))
		comp_a = intcode.Comp()
		comp_b = intcode.Comp()
		comp_c = intcode.Comp()
		comp_d = intcode.Comp()
		comp_e = intcode.Comp()
		sig_max = 0
		for temp_perm in phase_list:
			comp_a.load(mem_tape.copy())
			comp_b.load(mem_tape.copy())
			comp_c.load(mem_tape.copy())
			comp_d.load(mem_tape.copy())
			comp_e.load(mem_tape.copy())
			sig_a = comp_a.run([temp_perm[0], 0])
			sig_b = comp_b.run([temp_perm[1], sig_a])
			sig_c = comp_c.run([temp_perm[2], sig_b])
			sig_d = comp_d.run([temp_perm[3], sig_c])
			sig_e = comp_e.run([temp_perm[4], sig_d])
			if sig_e > sig_max:
				sig_max = sig_e
		return sig_max

	return ampl(file_in)

if __name__ == "__main__":
	print(run())