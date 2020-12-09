day_num = 9

file_load = open("input/input9.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split("\n")))

def run():

	def wrong(input_in):
		arr_curr = input_in[:25]
		arr_pos = 0
		for temp_check in input_in[25:]:
			arr_flag = False
			if not arr_flag:
				for temp_x in arr_curr:
					for temp_y in arr_curr:
						if temp_x != temp_y:
							if temp_x + temp_y == temp_check:
								arr_flag = True
			if not arr_flag:
				return temp_check
			arr_curr.pop(0)
			arr_curr.append(temp_check)

	def contig(input_in, input_find):
		hunt_len = 1
		while True:
			hunt_pos = 0
			while (hunt_pos + hunt_len) <= len(input_in):
				hunt_range = input_in[hunt_pos:hunt_pos + hunt_len + 1]
				if sum(hunt_range) == input_find:
					return min(hunt_range) + max(hunt_range)
				hunt_pos += 1
			hunt_len += 1

	return wrong(file_in), contig(file_in, wrong(file_in))