day_num = 1

file_load = open("input/input1.txt", "r")
file_in = file_load.read()
file_load.close()
file_in = list(map(int, file_in.split("\n")))

def run():

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

  return two(file_in), three(file_in)