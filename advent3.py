file_in = open("input.txt", "r").read().split("\n")

def slide(map_curr, slide_right, slide_left):
  pos_x = 0
  pos_y = 0
  tree_count = 0
  map_length = len(map_curr)
  map_width = len(map_curr[0])
  while(pos_y <= map_length):
    if map_curr[pos_y][pos_x] == "#":
      tree_count += 1
    pos_x += slide_right
    pos_y += slide_left
    if pos_y >= map_length:
      return tree_count
    if pos_x >= map_width:
      pos_x = pos_x % map_width
  return tree_count

print(slide(file_in, 3, 1))

slope_list = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
total_count = 1

for temp_test in slope_list:
  total_count = total_count * slide(file_in, temp_test[0], temp_test[1])

print(total_count)
