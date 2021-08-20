import intcode

day_num = 9

file_load = open("input/day9.txt", "r")
file_in = file_load.read()
file_load.close()

file_in = list(map(int, file_in.split(",")))

def run():

	def boost(input_in):
		mem_tape = input_in.copy()
		comp_main = intcode.Comp()
		comp_main.load(mem_tape)
		comp_main.run(input_dbg=True)
		print(comp_main.mem_out)
		return

	return boost(file_in)

if __name__ == "__main__":
	print(run())