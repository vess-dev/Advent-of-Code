file_in = list(map(int, open('input.txt', 'r').read().split("\n")))

def two(input_in):
  for temp_x in input_in:
    for temp_y in input_in:
      if temp_x != temp_y:
        if temp_x + temp_y == 2020:
          return temp_x * temp_y

def three(input_in):
  for temp_x in input_in:
    for temp_y in input_in:
      for temp_z in input_in:
        if temp_x != temp_y:
          if temp_y != temp_z:
            if temp_z != temp_x:
              if temp_x + temp_y + temp_z == 2020:
                return temp_x * temp_y * temp_z

print(two(file_in))
print(three(file_in))
