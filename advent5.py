file_load = open("input5.txt", "r")
file_in = file_load.read().split("\n")
file_load.close()

def run():

  def find(field_in):
    id_row = list(range(128))
    id_col= list(range(8))
    for temp_char in range(7):
      if field_in[temp_char] == "F":
        id_row = id_row[:len(id_row)//2]
      elif field_in[temp_char] == "B":
        id_row = id_row[len(id_row)//2:]
    for temp_char in range(3):
      if field_in[temp_char+7] == "L":
        id_col = id_col[:len(id_col)//2]
      elif field_in[temp_char+7] == "R":
        id_col = id_col[len(id_col)//2:]
    return id_row[0] * 8 + id_col[0]

  def high(input_in):
    id_max = 0
    for temp_field in input_in:
      test_field = find(temp_field)
      if test_field > id_max:
        id_max = test_field
    return id_max

  def missing(seat_ids):
      id_start = seat_ids[0]
      id_end = seat_ids[-1]
      seat_diff = sorted(set(range(id_start, id_end + 1)).difference(seat_ids))
      return seat_diff[0]

  def seat(input_in):
    seat_ids = []
    for temp_field in input_in:
      seat_ids.append(find(temp_field))
    return missing(sorted(seat_ids))

  return high(file_in), seat(file_in)