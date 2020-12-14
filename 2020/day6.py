day_num = 6

file_load = open("input/day6.txt", "r")
file_in = file_load.read()
file_load.close() 
file_in = file_in.split("\n\n")

def run():

	def yes(input_in):
		group_ans = [set(temp_group.replace("\n","")) for temp_group in input_in]
		group_total = 0
		for temp_group in group_ans:
			group_total += len(temp_group)
		return group_total

	def only(input_in):
		group_ans = [temp_group.split("\n") for temp_group in input_in]
		group_final = []
		for temp_group in group_ans:
			group_new = []
			for temp_person in temp_group:
				group_new.append(set(list(temp_person)))
			group_final.append(group_new[0].intersection(*group_new))
		group_total = 0
		for temp_group in group_final:
			group_total += len(temp_group)
		return group_total

	return yes(file_in), only(file_in)