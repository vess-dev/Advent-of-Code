day_num = 5

file_load = open("input/day5.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split(",")))

def run():

	def comp(input_in):
		mem_tape = input_in.copy()
		mem_pos = 0
		while True:
			com_pre = str(mem_tape[mem_pos])
			while len(com_pre) != 5:
				com_pre = "0" + com_pre
			com_mod = com_pre[:-2]
			com_op = com_pre[-2:]

			print(com_pre, com_mod, com_op)
			quit()
		

		return mem_tape

	def diag(input_in):
		return comp(input_in)

	return diag(file_in)

print(run())