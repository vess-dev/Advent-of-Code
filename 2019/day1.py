day_num = 1

file_load = open("input/day1.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split("\n")))