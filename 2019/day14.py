import collections
import math

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
					change_mult = math.ceil(input_list[temp_item] / input_in[temp_item][1]) 
					input_list[temp_item] -= input_in[temp_item][1] * change_mult
					for temp_change in input_in[temp_item][2]:
						input_list[temp_change[0]] += temp_change[1] * change_mult
		return input_list

	def chunk(input_in, input_list):
		while True:
			list_old = input_list.copy()
			input_list = cook(input_in, input_list)
			if input_list == list_old:
				break
		return input_list

	def bake(input_in):
		list_raw = collections.defaultdict(lambda: 0)
		list_raw["FUEL"] = 1
		list_raw = chunk(input_in, list_raw)
		return list_raw["ORE"]

	def swoop(input_in, input_list, input_fuel, input_change):
		while True:	
			input_list = chunk(input_in, input_list)
			input_list["FUEL"] = input_change
			if input_list["ORE"] < 1_000_000_000_000:
				input_fuel += input_change
			else:
				break
		return input_fuel - input_change

	def serve(input_in, input_one):
		list_raw = collections.defaultdict(lambda: 0)
		fuel_total = 1000000000000 // input_one
		list_raw["FUEL"] = fuel_total
		fuel_min = swoop(input_in, list_raw, fuel_total, 1000)
		list_raw = collections.defaultdict(lambda: 0)
		list_raw["FUEL"] = fuel_min
		fuel_max = swoop(input_in, list_raw, fuel_min, 1)
		return fuel_max

	fuel_one = bake(file_in)
	return fuel_one, serve(file_in, fuel_one)

if __name__ == "__main__":
	print(run())