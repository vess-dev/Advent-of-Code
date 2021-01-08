day_num = 21

file_load = open("input/day21.txt", "r")
file_in = file_load.read()
file_load.close()

file_in = file_in.replace(")","").replace("contains ","").replace(",","").split("\n")
for temp_itr, temp_item in enumerate(file_in):
	file_in[temp_itr] = file_in[temp_itr].split(" (")
	file_in[temp_itr][0] = file_in[temp_itr][0].split(" ")
	file_in[temp_itr][1] = file_in[temp_itr][1].split(" ")

def run():

	def solve(input_in):
		list_alg = {}
		for temp_line in input_in:
			for temp_alg in temp_line[1]:
				list_alg[temp_alg] = []
		for temp_line in input_in:
			for temp_alg in temp_line[1]:
				list_alg[temp_alg].append(temp_line[0])
		for temp_alg in list_alg:
			list_alg[temp_alg] = list(set(list_alg[temp_alg][0]).intersection(*list_alg[temp_alg]))
		alg_done = set()
		while any(len(list_alg[temp_alg]) != 1 for temp_alg in list_alg):
			for temp_alg in list_alg:
				if len(list_alg[temp_alg]) == 1:
					alg_done.add(list_alg[temp_alg][0])
				else:
					list_alg[temp_alg] = [temp_check for temp_check in list_alg[temp_alg] if temp_check not in alg_done]
		return list_alg
	
	def safe(input_in):
		list_alg = solve(input_in)
		list_ing = [temp_itr[0] for temp_itr in list(list_alg.values())]
		total_ing = 0
		for temp_line in input_in:
			for temp_ing in temp_line[0]:
				if temp_ing not in list_ing:
					total_ing += 1
		return total_ing

	def order(input_in):
		list_alg = solve(input_in)
		list_sort = sorted(list(list_alg.keys()))
		total_string = ""
		for temp_alg in list_sort:
			total_string += list_alg[temp_alg][0] + ","
		return total_string[:-1]

	return safe(file_in), order(file_in)