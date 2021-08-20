import textwrap

day_num = 8

file_load = open("input/day8.txt", "r")
file_in = file_load.read()
file_load.close()

def run():

	def layer(input_in, input_size):
		layer_count = input_size[0] * input_size[1]
		layer_data = textwrap.wrap(input_in, layer_count)
		layer_zeroes = []
		for temp_layer in layer_data:
			layer_zeroes.append(temp_layer.count("0"))
		layer_most = layer_data[layer_zeroes.index(min(layer_zeroes))]
		return layer_most.count("1") * layer_most.count("2")

	def decode(input_in, input_size):
		layer_count = input_size[0] * input_size[1]
		layer_data = textwrap.wrap(input_in, layer_count)
		print(layer_data)

	#return layer(file_in, [25, 6]), decode(file_in, [25, 6])
	return decode(file_in, [2, 2])

if __name__ == "__main__":
	print(run())