file_in = list(map(int, open('input.txt', 'r').read().split("\n")))

for temp_x in file_in:
  for temp_y in file_in:
    if temp_x != temp_y:
      if temp_x + temp_y == 2020:
        print(temp_x * temp_y)

for temp_x in file_in:
  for temp_y in file_in:
    for temp_z in file_in:
      if temp_x != temp_y:
        if temp_y != temp_z:
          if temp_z != temp_x:
            if temp_x + temp_y + temp_z == 2020:
              print(temp_x * temp_y * temp_z)
