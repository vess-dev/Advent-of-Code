file_in = open('input.txt', 'r').read().replace(":", "").split("\n")

pass_total = len(file_in)
pass_valid = 0

for temp_test in file_in:
  temp_split = temp_test.split(" ")
  temp_min = int(temp_split[0].split("-")[0])
  temp_max = int(temp_split[0].split("-")[1])
  temp_count = temp_split[2].count(temp_split[1])
  if temp_count >= temp_min and temp_count <= temp_max:
    pass_valid += 1

print(pass_valid)
pass_valid = 0

for temp_test in file_in:
  temp_split = temp_test.split(" ")
  temp_fst = int(temp_split[0].split("-")[0]) - 1
  temp_sec = int(temp_split[0].split("-")[1]) - 1
  if (temp_split[2][temp_fst] == temp_split[1]) is not (temp_split[2][temp_sec] == temp_split[1]):
    pass_valid += 1

print(pass_valid)
