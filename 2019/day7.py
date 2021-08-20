import intcode
import itertools

day_num = 7

file_load = open("input/day7.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split(",")))

def run():

	def five():
		return intcode.Comp(), intcode.Comp(), intcode.Comp(), intcode.Comp(), intcode.Comp()

	def ampl(input_in):
		mem_tape = input_in.copy()
		phase_list = list(itertools.permutations([0, 1, 2, 3, 4]))
		comp_a, comp_b, comp_c, comp_d, comp_e = five()
		comp_all = [comp_a, comp_b, comp_c, comp_d, comp_e]
		sig_max = 0
		for temp_perm in phase_list:
			for temp_comp in comp_all:
				temp_comp.load(mem_tape.copy())
			sig_a = comp_a.run([temp_perm[0], 0])
			sig_b = comp_b.run([temp_perm[1], sig_a])
			sig_c = comp_c.run([temp_perm[2], sig_b])
			sig_d = comp_d.run([temp_perm[3], sig_c])
			sig_e = comp_e.run([temp_perm[4], sig_d])
			if sig_e > sig_max:
				sig_max = sig_e
		return sig_max

	def loop(input_in):
		mem_tape = input_in.copy()
		phase_list = list(itertools.permutations([5, 6, 7, 8, 9]))
		comp_a, comp_b, comp_c, comp_d, comp_e = five()
		comp_all = [comp_a, comp_b, comp_c, comp_d, comp_e]
		sig_max = 0
		for temp_perm in phase_list:
			for temp_comp in comp_all:
				temp_comp.load(mem_tape.copy())
			flag_pipe = False
			ret_e = 0
			while not comp_e.flag_halt:
				ret_a = comp_a.next()
				if ret_a == "Input" and not flag_pipe:
					comp_a.take(temp_perm[0], 0)
					flag_pipe = True
				elif ret_a == "Input" and flag_pipe:
					comp_a.take(temp_perm[0], ret_e)

			quit()
		return

	#return ampl(file_in), loop(file_in)
	#return ampl(file_in)
	return loop(file_in)

if __name__ == "__main__":
	print(run())