file_in = open("input.txt", "r").read().replace(":", "").split("\n")

def test(input_in): 
  test_fst, test_sec = 0, 0
  for temp_test in input_in:
    temp_split = temp_test.split(" ")
    temp_min = int(temp_split[0].split("-")[0])
    temp_max = int(temp_split[0].split("-")[1])
    temp_fst = int(temp_split[0].split("-")[0]) - 1
    temp_sec = int(temp_split[0].split("-")[1]) - 1
    temp_count = temp_split[2].count(temp_split[1])
    if temp_count >= temp_min and temp_count <= temp_max:
      test_fst += 1
    if (temp_split[2][temp_fst] == temp_split[1]) is not (temp_split[2][temp_sec] == temp_split[1]):
      test_sec += 1
  return test_fst, test_sec

print(test(file_in))
