from collections import OrderedDict

day_num = 7

file_load = open("input/input7.txt", "r")
file_in = file_load.read()
file_load.close() 
file_in = file_in.replace(",","")
file_in = file_in.replace(".","")
file_in = file_in.replace("bags ", "")
file_in = file_in.replace("contain ", "")
file_in = file_in.replace("bags", "")
file_in = file_in.replace("bag ", "")
file_in = file_in.replace("bag", "")
file_in = file_in.split("\n")
file_in = [temp_bag[:-1] for temp_bag in file_in]

file_new = []
for temp_bags in file_in:
	temp_hold = []
	iter_bag = iter(temp_bags.split(" "))
	temp_hold.append(next(iter_bag) + " " + next(iter_bag))
	while True:
		try:
			bag_num = int(next(iter_bag))
			bag_glint = next(iter_bag)
			bag_color = next(iter_bag)
			for temp_count in range(bag_num):
				temp_hold.append(bag_glint + " " + bag_color)
		except:
			break
	file_new.append(temp_hold)

file_in = []
for temp_bags in file_new:
	file_in.append(list(OrderedDict.fromkeys(temp_bags)))
input_search = [temp_bags[0] for temp_bags in file_in]
file_in.pop(input_search.index("shiny gold"))
file_in = [temp_bags for temp_bags in file_in if len(temp_bags) != 1]

def run():

	def size(input_in, bag_search):
		size_weight = 1
		input_search = [temp_bags[0] for temp_bags in input_in]
		bag_check = input_in[input_search.index(bag_search)]
		if len(bag_check) == 1:
			return 1
		else:
			for temp_each in bag_check[1:]:
				size_weight += size(input_in, temp_each)
			return size_weight

	def shiny(input_in):
		bag_verif = []
		for temp_bags in input_in:
			if "shiny gold" in temp_bags:
				bag_verif.append(temp_bags[0])
		while True:
			bag_flag = False
			for temp_bags in input_in:
				if temp_bags[0] not in bag_verif:
					if any(temp_check in temp_bags for temp_check in bag_verif):
						bag_verif = [temp_bags[0]] + bag_verif
						input_in.pop(input_in.index(temp_bags))
						bag_flag = True
			if not bag_flag:
				return len(bag_verif)

	def weight(input_in):
		bag_weight = 0
		input_search = [temp_bags[0] for temp_bags in input_in]
		for temp_bag in input_in[input_search.index("shiny gold")][1:]:
			bag_weight += size(input_in, temp_bag)
		return bag_weight

	return shiny(file_in.copy()), weight(file_new)