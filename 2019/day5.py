import intcode

day_num = 5

file_load = open("input/day5.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split(",")))

def run():

	def diag(input_in):
		comp_result = comp(input_in, 1)
		comp_result = comp_result.split(" ")
		return comp_result[-1]

	def test(input_in):
		comp_result = comp(input_in, 5)
		return comp_result

	return diag(file_in)#, test(file_in)

if __name__ == "__main__":
	print(run())