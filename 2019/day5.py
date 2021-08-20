import intcode

day_num = 5

file_load = open("input/day5.txt", "r")
file_in = file_load.read()
file_load.close()

file_in = list(map(int, file_in.split(",")))

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