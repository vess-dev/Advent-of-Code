import collections

day_num = 14

file_load = open("input/day14.txt", "r")
file_prep = file_load.read()
file_load.close()

file_in = {}
file_prep = file_prep.split("\n")
for temp_line in file_prep:
	mix_pair = temp_line.split(" => ")
	mix_in = mix_pair[0]
	mix_in = mix_in.split(", ")
	mix_in = [(temp_part.split(" ")[1], int(temp_part.split(" ")[0])) for temp_part in mix_in]
	mix_out = mix_pair[1]
	mix_out = mix_out.split(" ")
	file_in[mix_out[1]] = [0, int(mix_out[0]), mix_in]

def distance(input_in, input_key, input_distance):
	input_in[input_key][0] = input_distance
	for temp_rule in input_in[input_key][2]:
		if temp_rule[0] != "ORE":
			distance(input_in, temp_rule[0], input_distance + 1)
	return

for temp_rule in file_in["FUEL"][2]:
	distance(file_in, temp_rule[0], 1)
file_in = dict(sorted(file_in.items(), key=lambda temp_rule: temp_rule[1][0]))

def run():

	def cook(input_in, input_list):
		list_keys = list(input_list.keys())
		for temp_item in list_keys:
			if temp_item != "ORE":
				if input_list[temp_item] > 0:
					while input_list[temp_item] >= input_in[temp_item][1]:
						input_list[temp_item] -= input_in[temp_item][1]
						for temp_change in input_in[temp_item][2]:
							input_list[temp_change[0]] += temp_change[1]
		return input_list

	def bake(input_in):
		print(input_in)
		print()
		list_raw = collections.defaultdict(lambda: 0)
		list_raw["FUEL"] = 1
		while True:
			print(list_raw)
			list_old = list_raw.copy()
			list_raw = cook(input_in, list_raw)
			if list_raw == list_old:
				if any(list_raw[temp_item] > 0 for temp_item in list_raw if temp_item != "ORE"):
					for temp_rule in input_in:
						if list_raw[temp_rule] > 0:
							list_raw[temp_rule] = 0
							for temp_change in input_in[temp_rule][2]:
								list_raw[temp_change[0]] += temp_change[1]
							break
				else:
					break
		return list_raw["ORE"]

	return bake(file_in)

if __name__ == "__main__":
	print(run())

#any(list_raw[temp_item] > 0 for temp_item in list_raw if temp_item != "ORE")