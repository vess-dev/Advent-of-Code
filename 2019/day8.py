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
		layer_image = [""] * layer_count
		for temp_row in layer_data:
			for temp_num, temp_col in enumerate(temp_row):
				layer_image[temp_num % len(temp_row)] += temp_col
		for temp_idx, temp_slice in enumerate(layer_image):
			new_slice = temp_slice.replace("2", "")[0]
			new_slice = new_slice.replace("0", " ")
			new_slice = new_slice.replace("1", "*")
			layer_image[temp_idx] = new_slice
		print(" ", end="")
		for temp_idx, temp_char in enumerate(layer_image, start=1):
			if temp_idx % input_size[0] == 0:
				print(temp_char, end="\n ")
			else:
				print(temp_char, end="")
		print()
		return

	return layer(file_in, [25, 6]), decode(file_in, [25, 6])

if __name__ == "__main__":
	print(run())