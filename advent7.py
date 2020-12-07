from collections import OrderedDict

file_load = open("input7.txt", "r")
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

file_other = []
for temp_bags in file_new:
	file_other.append(list(OrderedDict.fromkeys(temp_bags)))

def run():

	def probe(input_in, bag_search, bag_verif, bag_ugly):
		input_search = [temp_bags[0] for temp_bags in input_in]
		bag_check = input_in[input_search.index(bag_search)]
		if len(bag_check) == 1:
			return False
		else:
			if "shiny gold" in bag_check:
				return True
			else:
				for temp_each in bag_check[1:]:
					if temp_each in bag_verif:
						return True
					else:
						if temp_each not in bag_ugly:
							if probe(input_in, temp_each, bag_verif, bag_ugly):
								return True

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

	def tree(input_in):
		bag_verif = []
		bag_ugly = []
		input_search = [temp_bags[0] for temp_bags in input_in]
		input_in.pop(input_search.index("shiny gold"))
		for temp_bags in input_in:
			if "shiny gold" in temp_bags:
				bag_verif.append(temp_bags[0])
			else:
				for temp_bag in temp_bags:
					if temp_bag not in bag_verif:
						if temp_bag not in bag_ugly:
							if probe(input_in, temp_bag, bag_verif, bag_ugly):
								bag_verif.append(temp_bags[0])
							else:
								bag_ugly.append(temp_bags[0])
		return len(set(bag_verif))

	def weight(input_in):
		bag_weight = 0
		input_search = [temp_bags[0] for temp_bags in input_in]
		for temp_bag in input_in[input_search.index("shiny gold")][1:]:
			bag_weight += size(input_in, temp_bag)
		return bag_weight

	return tree(file_other.copy()), weight(file_new)

print(run())