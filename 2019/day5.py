import intcode

day_num = 5

file_load = open("input/day5.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split(",")))

def run():

	def diag(input_in):
		mem_tape = input_in.copy()
		obj_comp = intcode.Comp()
		obj_comp.load(mem_tape)
		while True:
			comp_ret = obj_comp.next()
			if comp_ret == "Input":
				obj_comp.take(1)
			elif comp_ret == "Break":
				break
		return obj_comp.mem_stdout[-1]

	def test(input_in):
		mem_tape = input_in.copy()
		obj_comp = intcode.Comp()
		obj_comp.load(mem_tape)
		while True:
			comp_ret = obj_comp.next()
			if comp_ret == "Input":
				obj_comp.take(5)
			elif comp_ret == "Break":
				break
		return obj_comp.mem_stdout[-1]

	return diag(file_in), test(file_in)

if __name__ == "__main__":
	print(run())